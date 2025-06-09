"""
Modelo de Usuario para MongoDB
"""
from datetime import datetime
from bson import ObjectId
from config.database import get_db
from pymongo.errors import DuplicateKeyError
import re

class User:
    """Modelo de Usuario"""
    
    def __init__(self, full_name=None, email=None, password=None, **kwargs):
        self.full_name = full_name
        self.email = email.lower() if email else None
        self.password = password
        self.created_at = kwargs.get('created_at', datetime.utcnow())
        self.updated_at = kwargs.get('updated_at', datetime.utcnow())
        self._id = kwargs.get('_id', None)
    
    @staticmethod
    def get_collection():
        """Obtener la colección de usuarios"""
        db = get_db()
        return db.users
    
    def save(self):
        """Guardar usuario en la base de datos"""
        collection = self.get_collection()
        
        # Crear índice único para email si no existe
        collection.create_index("email", unique=True)
        
        user_data = {
            'fullName': self.full_name,
            'email': self.email,
            'password': self.password,
            'createdAt': self.created_at,
            'updatedAt': datetime.utcnow()
        }
        
        try:
            if self._id:
                # Actualizar usuario existente
                result = collection.update_one(
                    {'_id': ObjectId(self._id)},
                    {'$set': user_data}
                )
                return self._id
            else:
                # Crear nuevo usuario
                result = collection.insert_one(user_data)
                self._id = result.inserted_id
                return self._id
                
        except DuplicateKeyError:
            raise ValueError('El correo ya está registrado')
    
    @staticmethod
    def find_by_email(email):
        """Buscar usuario por email"""
        collection = User.get_collection()
        user_data = collection.find_one({'email': email.lower()})
        
        if user_data:
            return User(
                full_name=user_data['fullName'],
                email=user_data['email'],
                password=user_data['password'],
                created_at=user_data.get('createdAt'),
                updated_at=user_data.get('updatedAt'),
                _id=str(user_data['_id'])
            )
        return None
    
    @staticmethod
    def find_by_id(user_id):
        """Buscar usuario por ID"""
        collection = User.get_collection()
        user_data = collection.find_one({'_id': ObjectId(user_id)})
        
        if user_data:
            return User(
                full_name=user_data['fullName'],
                email=user_data['email'],
                password=user_data['password'],
                created_at=user_data.get('createdAt'),
                updated_at=user_data.get('updatedAt'),
                _id=str(user_data['_id'])
            )
        return None
    
    def to_dict(self, include_password=False):
        """Convertir usuario a diccionario para respuesta JSON"""
        user_dict = {
            '_id': str(self._id),
            'fullName': self.full_name,
            'email': self.email,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }
        
        if include_password:
            user_dict['password'] = self.password
            
        return user_dict
    
    @staticmethod
    def validate_email(email):
        """Validar formato de email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
