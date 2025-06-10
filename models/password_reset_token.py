"""
Modelo para tokens de restablecimiento de contraseña
"""
from datetime import datetime, timedelta
from bson import ObjectId
from config.database import get_db
import secrets
import hashlib

class PasswordResetToken:
    """Modelo para tokens de restablecimiento de contraseña"""
    
    def __init__(self, user_id=None, token=None, expires_at=None, used=False, **kwargs):
        self.user_id = user_id
        self.token = token
        self.expires_at = expires_at or datetime.utcnow() + timedelta(hours=1)  # Expira en 1 hora
        self.used = used
        self.created_at = kwargs.get('created_at', datetime.utcnow())
        self._id = kwargs.get('_id', None)
    
    @staticmethod
    def get_collection():
        """Obtener la colección de tokens de reset"""
        db = get_db()
        return db.password_reset_tokens
    
    @staticmethod
    def generate_token():
        """Generar un token seguro de 32 caracteres"""
        # Generar token aleatorio
        random_token = secrets.token_urlsafe(32)
        # Hash del token para almacenamiento seguro
        token_hash = hashlib.sha256(random_token.encode()).hexdigest()
        return random_token, token_hash
    
    def save(self):
        """Guardar token en la base de datos"""
        collection = self.get_collection()
        
        # Crear índice TTL para auto-eliminación de tokens expirados
        collection.create_index("expires_at", expireAfterSeconds=0)
        
        token_data = {
            'user_id': ObjectId(self.user_id),
            'token': self.token,
            'expires_at': self.expires_at,
            'used': self.used,
            'created_at': self.created_at
        }
        
        if self._id:
            # Actualizar token existente
            result = collection.update_one(
                {'_id': ObjectId(self._id)},
                {'$set': token_data}
            )
            return self._id
        else:
            # Crear nuevo token
            result = collection.insert_one(token_data)
            self._id = result.inserted_id
            return self._id
    
    @staticmethod
    def find_by_token(token_hash):
        """Buscar token por hash"""
        collection = PasswordResetToken.get_collection()
        token_data = collection.find_one({
            'token': token_hash,
            'used': False,
            'expires_at': {'$gt': datetime.utcnow()}
        })
        
        if token_data:
            return PasswordResetToken(
                user_id=str(token_data['user_id']),
                token=token_data['token'],
                expires_at=token_data['expires_at'],
                used=token_data['used'],
                created_at=token_data.get('created_at'),
                _id=str(token_data['_id'])
            )
        return None
    
    @staticmethod
    def invalidate_user_tokens(user_id):
        """Invalidar todos los tokens activos de un usuario"""
        collection = PasswordResetToken.get_collection()
        collection.update_many(
            {
                'user_id': ObjectId(user_id),
                'used': False,
                'expires_at': {'$gt': datetime.utcnow()}
            },
            {'$set': {'used': True}}
        )
    
    def mark_as_used(self):
        """Marcar token como usado"""
        self.used = True
        return self.save()
    
    def is_valid(self):
        """Verificar si el token es válido"""
        return (
            not self.used and 
            self.expires_at > datetime.utcnow()
        )
