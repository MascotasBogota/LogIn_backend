"""
Controlador para restablecimiento de contraseñas
"""
import bcrypt
from flask import current_app
from models.user import User
from models.password_reset_token import PasswordResetToken
from services.email_service import EmailService
import hashlib

class PasswordResetController:
    """Controlador para operaciones de restablecimiento de contraseña"""
    
    @staticmethod
    def request_password_reset(request_data):
        """
        Solicitar restablecimiento de contraseña
        
        Args:
            request_data (dict): Datos del request con email
            
        Returns:
            tuple: (response_data, status_code)
        """
        try:
            email = request_data.get('email', '').strip().lower()
            
            print(f'🔐 Solicitud de reset para: {email}')
            
            # Validar que el email esté presente
            if not email:
                return {'message': 'El correo electrónico es obligatorio'}, 400
            
            # Validar formato de email
            if not User.validate_email(email):
                return {'message': 'El formato del correo electrónico no es válido'}, 400
            
            # Buscar usuario por email
            user = User.find_by_email(email)
            
            if not user:
                print(f'❌ Usuario no encontrado: {email}')
                # Por seguridad, no revelamos si el email existe o no
                return {
                    'message': 'Si el correo está registrado, recibirás un enlace para restablecer tu contraseña'
                }, 200
            
            print(f'✅ Usuario encontrado: {user.full_name}')
            
            # Invalidar tokens existentes del usuario
            PasswordResetToken.invalidate_user_tokens(user._id)
            
            # Generar nuevo token
            raw_token, token_hash = PasswordResetToken.generate_token()
            
            # Crear registro del token en la base de datos
            reset_token = PasswordResetToken(
                user_id=user._id,
                token=token_hash
            )
            
            token_id = reset_token.save()
            print(f'✅ Token generado: {token_id}')
            
            # Enviar email de restablecimiento
            email_sent = EmailService.send_password_reset_email(
                user_email=user.email,
                user_name=user.full_name,
                reset_token=raw_token  # Enviamos el token sin hash
            )
            
            if email_sent:
                print(f'✅ Email enviado a: {email}')
                return {
                    'message': 'Si el correo está registrado, recibirás un enlace para restablecer tu contraseña'
                }, 200
            else:
                print(f'❌ Error enviando email a: {email}')
                return {
                    'message': 'Error enviando email. Intenta nuevamente más tarde'
                }, 500
                
        except Exception as e:
            print(f'❌ Error en request_password_reset: {e}')
            return {
                'message': 'Error procesando solicitud',
                'error': str(e)
            }, 500
    
    @staticmethod
    def verify_reset_token(request_data):
        """
        Verificar si un token de reset es válido
        
        Args:
            request_data (dict): Datos del request con token
            
        Returns:
            tuple: (response_data, status_code)
        """
        try:
            token = request_data.get('token', '').strip()
            
            if not token:
                return {'message': 'Token requerido'}, 400
            
            # Hash del token para búsqueda
            token_hash = hashlib.sha256(token.encode()).hexdigest()
            
            # Buscar token en la base de datos
            reset_token = PasswordResetToken.find_by_token(token_hash)
            
            if not reset_token or not reset_token.is_valid():
                return {
                    'message': 'Token inválido o expirado',
                    'valid': False
                }, 400
            
            # Buscar usuario asociado
            user = User.find_by_id(reset_token.user_id)
            
            if not user:
                return {
                    'message': 'Usuario no encontrado',
                    'valid': False
                }, 400
            
            return {
                'message': 'Token válido',
                'valid': True,
                'user_email': user.email
            }, 200
            
        except Exception as e:
            print(f'❌ Error en verify_reset_token: {e}')
            return {
                'message': 'Error verificando token',
                'error': str(e)
            }, 500
    
    @staticmethod
    def reset_password(request_data):
        """
        Restablecer contraseña con token válido
        
        Args:
            request_data (dict): Datos del request con token y nueva contraseña
            
        Returns:
            tuple: (response_data, status_code)
        """
        try:
            token = request_data.get('token', '').strip()
            new_password = request_data.get('password', '')
            
            print(f'🔐 Restablecimiento de contraseña con token')
            
            # Validaciones básicas
            if not token:
                return {'message': 'Token requerido'}, 400
            
            if not new_password:
                return {'message': 'La nueva contraseña es obligatoria'}, 400
            
            # Validar longitud de contraseña
            if len(new_password) < 6:
                return {'message': 'La contraseña debe tener al menos 6 caracteres'}, 400
            
            # Validar fortaleza de contraseña (misma validación que registro)
            import re
            pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)'
            if not re.match(pattern, new_password):
                return {
                    'message': 'La contraseña debe contener al menos una mayúscula, una minúscula y un número'
                }, 400
            
            # Hash del token para búsqueda
            token_hash = hashlib.sha256(token.encode()).hexdigest()
            
            # Buscar y validar token
            reset_token = PasswordResetToken.find_by_token(token_hash)
            
            if not reset_token or not reset_token.is_valid():
                return {
                    'message': 'Token inválido o expirado'
                }, 400
            
            # Buscar usuario
            user = User.find_by_id(reset_token.user_id)
            
            if not user:
                return {'message': 'Usuario no encontrado'}, 400
            
            # Hashear nueva contraseña
            password_bytes = new_password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password_bytes, salt).decode('utf-8')
            
            # Actualizar contraseña del usuario
            user.password = hashed_password
            user.save()
            
            # Marcar token como usado
            reset_token.mark_as_used()
            
            # Invalidar todos los demás tokens del usuario
            PasswordResetToken.invalidate_user_tokens(user._id)
            
            print(f'✅ Contraseña restablecida para: {user.email}')
            
            return {
                'message': 'Contraseña restablecida exitosamente'
            }, 200
            
        except Exception as e:
            print(f'❌ Error en reset_password: {e}')
            return {
                'message': 'Error restableciendo contraseña',
                'error': str(e)
            }, 500
