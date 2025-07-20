"""
Controlador para manejo de usuarios
"""
import bcrypt
import jwt
import os
from datetime import datetime, timedelta
from flask import current_app, jsonify
from models.user import User
from services.user_creation_validation import create_user_validation_chain

class UserController:
    """Controlador para operaciones de usuario"""
    
    @staticmethod
    async def register_user(request_data):
        """Registrar un nuevo usuario"""
        try:
            # Obtener datos del request
            full_name = request_data.get('full_name', '').strip() # Cambiado a full_name
            email = request_data.get('email', '').strip()
            password = request_data.get('password', '')
            
            print(f'📝 Datos recibidos para registro: full_name={full_name}, email={email}, password=***')
            
            # Crear cadena de validación
            validation_chain = create_user_validation_chain()
            
            # Variable para capturar la respuesta de validación
            validation_response = {'sent': False, 'data': None, 'status': None}
            
            def response_handler(data, status_code):
                """Handler para capturar respuestas de validación"""
                validation_response['sent'] = True
                validation_response['data'] = data
                validation_response['status'] = status_code
            
            # Ejecutar validaciones
            validation_passed = await validation_chain.handle(request_data, response_handler)
            
            # Si las validaciones fallaron, retornar el error
            if not validation_passed or validation_response['sent']:
                print('❌ Validaciones fallaron')
                return validation_response['data'], validation_response['status']
            
            print('✅ Validaciones pasaron, creando usuario...')
            
            # Hashear la contraseña
            password_bytes = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password_bytes, salt).decode('utf-8')
            
            # Crear el usuario
            user = User(
                full_name=full_name, # Usar full_name
                email=email,
                password=hashed_password
            )
            
            user_id = user.save()
            print(f'✅ Usuario creado: {user_id}')
            
            # Responder con el usuario creado (sin la contraseña)
            return user.to_dict(), 201
            
        except ValueError as e:
            print(f'❌ Error de validación: {e}')
            return {'message': str(e)}, 400
        except Exception as e:
            print(f'❌ Error en register_user: {e}')
            return {
                'message': 'Error al registrar usuario',
                'error': str(e)
            }, 500
    
    @staticmethod
    def login_user(request_data):
        """Iniciar sesión de usuario"""
        try:
            email = request_data.get('email', '').strip()
            password = request_data.get('password', '')
            
            print(f'🔐 Intento de login para: {email}')
            
            # Validar que todos los campos estén presentes
            if not email or not password:
                return {'message': 'Todos los campos son obligatorios'}, 400
            
            # Buscar el usuario por email
            user = User.find_by_email(email)
            print(f'🔍 Usuario encontrado: {"Sí" if user else "No"}')
            
            if not user:
                return {'message': 'Credenciales inválidas'}, 400
            
            # Verificar la contraseña
            password_bytes = password.encode('utf-8')
            stored_password_bytes = user.password.encode('utf-8')
            is_match = bcrypt.checkpw(password_bytes, stored_password_bytes)
            print(f'🔐 Contraseña válida: {"Sí" if is_match else "No"}')
            
            if not is_match:
                return {'message': 'Credenciales inválidas'}, 400
            
            # Crear el token JWT
            secret_key = os.getenv('JWT_SECRET', 'mascotas_secret_key')  # Usar JWT_SECRET directamente
            payload = {
                'sub': str(user._id),  # Usar 'sub' (subject) estándar JWT
                'userId': str(user._id),  # Mantener por compatibilidad
                'exp': datetime.utcnow() + timedelta(days=30),
                'iat': datetime.utcnow(),  # Issued at
                'type': 'access'  # Tipo de token
            }
            
            token = jwt.encode(payload, secret_key, algorithm='HS256')
            
            print(f'✅ Login exitoso para: {email}')
            
            return {
                'token': token,
                'user': user.to_dict()
            }, 200
            
        except Exception as e:
            print(f'❌ Error en login_user: {e}')
            return {
                'message': 'Error al iniciar sesión',
                'error': str(e)
            }, 500
