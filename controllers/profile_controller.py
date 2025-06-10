"""
Controlador para gestión de perfil de usuario
"""
import bcrypt
import jwt
from datetime import datetime
from flask import current_app
from models.user import User
import re

class ProfileController:
    """Controlador para operaciones de perfil de usuario"""
    
    @staticmethod
    def get_profile(user_id):
        """
        Obtener información del perfil del usuario
        
        Args:
            user_id (str): ID del usuario
            
        Returns:
            tuple: (response_data, status_code)
        """
        try:
            print(f'📋 Obteniendo perfil para usuario: {user_id}')
            
            # Buscar usuario por ID
            user = User.find_by_id(user_id)
            
            if not user:
                return {'message': 'Usuario no encontrado'}, 404
            
            # Retornar datos del perfil (sin contraseña)
            profile_data = user.to_dict(include_password=False)
            
            # Agregar indicador de contraseña protegida
            profile_data['hasPassword'] = bool(user.password)
            
            print(f'✅ Perfil obtenido para: {user.email}')
            
            return {
                'message': 'Perfil obtenido exitosamente',
                'profile': profile_data
            }, 200
            
        except Exception as e:
            print(f'❌ Error en get_profile: {e}')
            return {
                'message': 'Error obteniendo perfil',
                'error': str(e)
            }, 500
    
    @staticmethod
    def update_profile(user_id, request_data):
        """
        Actualizar información del perfil del usuario
        
        Args:
            user_id (str): ID del usuario
            request_data (dict): Datos a actualizar
            
        Returns:
            tuple: (response_data, status_code)
        """
        try:
            print(f'📝 Actualizando perfil para usuario: {user_id}')
            
            # Buscar usuario existente
            user = User.find_by_id(user_id)
            
            if not user:
                return {'message': 'Usuario no encontrado'}, 404
            
            # Validar y procesar campos a actualizar
            validation_result = ProfileController._validate_profile_data(request_data, user)
            if validation_result['has_errors']:
                return {'message': validation_result['message']}, 400
            
            # Actualizar campos del usuario
            updated_fields = []
            
            # Campos básicos
            if 'fullName' in request_data:
                full_name = request_data['fullName'].strip()
                if len(full_name) >= 2:
                    user.full_name = full_name
                    updated_fields.append('fullName')
                else:
                    return {'message': 'El nombre debe tener al menos 2 caracteres'}, 400
            
            if 'email' in request_data:
                email = request_data['email'].strip().lower()
                if User.validate_email(email):
                    # Verificar que el email no esté en uso por otro usuario
                    existing_user = User.find_by_email(email)
                    if existing_user and existing_user._id != user._id:
                        return {'message': 'El correo ya está en uso por otro usuario'}, 400
                    user.email = email
                    updated_fields.append('email')
                else:
                    return {'message': 'Formato de correo inválido'}, 400
            
            # Campos opcionales
            if 'username' in request_data:
                username = request_data['username'].strip() if request_data['username'] else None
                if username:
                    if User.validate_username(username):
                        # Verificar que el username no esté en uso
                        existing_user = User.find_by_username(username)
                        if existing_user and existing_user._id != user._id:
                            return {'message': 'El nombre de usuario ya está en uso'}, 400
                        user.username = username
                        updated_fields.append('username')
                    else:
                        return {
                            'message': 'Username inválido. Debe tener 3-20 caracteres y solo letras, números y guiones bajos'
                        }, 400
                else:
                    user.username = None
                    updated_fields.append('username')
            
            if 'profilePicture' in request_data:
                user.profile_picture = request_data['profilePicture']
                updated_fields.append('profilePicture')
            
            if 'gender' in request_data:
                gender = request_data['gender']
                if User.validate_gender(gender):
                    user.gender = gender.lower() if gender else None
                    updated_fields.append('gender')
                else:
                    return {
                        'message': 'Género inválido. Opciones: male, female, other, prefer_not_to_say'
                    }, 400
            
            if 'address' in request_data:
                address = request_data['address'].strip() if request_data['address'] else None
                if User.validate_address(address):
                    user.address = address
                    updated_fields.append('address')
                else:
                    return {'message': 'Dirección inválida. Debe tener entre 5 y 200 caracteres'}, 400
            
            if 'phoneNumber' in request_data:
                phone = request_data['phoneNumber'].strip() if request_data['phoneNumber'] else None
                if User.validate_phone_number(phone):
                    user.phone_number = phone
                    updated_fields.append('phoneNumber')
                else:
                    return {'message': 'Número de teléfono inválido'}, 400
            
            # Actualizar timestamp
            user.updated_at = datetime.utcnow()
            
            # Guardar cambios
            user.save()
            
            print(f'✅ Perfil actualizado. Campos: {", ".join(updated_fields)}')
            
            # Retornar perfil actualizado
            return {
                'message': 'Perfil actualizado exitosamente',
                'profile': user.to_dict(include_password=False),
                'updatedFields': updated_fields
            }, 200
            
        except ValueError as e:
            print(f'❌ Error de validación: {e}')
            return {'message': str(e)}, 400
        except Exception as e:
            print(f'❌ Error en update_profile: {e}')
            return {
                'message': 'Error actualizando perfil',
                'error': str(e)
            }, 500
    
    @staticmethod
    def change_password(user_id, request_data):
        """
        Cambiar contraseña del usuario
        
        Args:
            user_id (str): ID del usuario
            request_data (dict): Datos con contraseña actual y nueva
            
        Returns:
            tuple: (response_data, status_code)
        """
        try:
            current_password = request_data.get('currentPassword', '')
            new_password = request_data.get('newPassword', '')
            
            print(f'🔐 Cambio de contraseña para usuario: {user_id}')
            
            # Validaciones básicas
            if not current_password or not new_password:
                return {'message': 'Contraseña actual y nueva son obligatorias'}, 400
            
            # Buscar usuario
            user = User.find_by_id(user_id)
            if not user:
                return {'message': 'Usuario no encontrado'}, 404
            
            # Verificar contraseña actual
            current_password_bytes = current_password.encode('utf-8')
            stored_password_bytes = user.password.encode('utf-8')
            is_current_valid = bcrypt.checkpw(current_password_bytes, stored_password_bytes)
            
            if not is_current_valid:
                return {'message': 'Contraseña actual incorrecta'}, 400
            
            # Validar nueva contraseña
            if len(new_password) < 6:
                return {'message': 'La nueva contraseña debe tener al menos 6 caracteres'}, 400
            
            # Validar fortaleza de contraseña
            pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)'
            if not re.match(pattern, new_password):
                return {
                    'message': 'La nueva contraseña debe contener al menos una mayúscula, una minúscula y un número'
                }, 400
            
            # Verificar que la nueva contraseña sea diferente
            new_password_bytes = new_password.encode('utf-8')
            is_same_password = bcrypt.checkpw(new_password_bytes, stored_password_bytes)
            if is_same_password:
                return {'message': 'La nueva contraseña debe ser diferente a la actual'}, 400
            
            # Hashear nueva contraseña
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(new_password_bytes, salt).decode('utf-8')
            
            # Actualizar contraseña
            user.password = hashed_password
            user.updated_at = datetime.utcnow()
            user.save()
            
            print(f'✅ Contraseña cambiada para: {user.email}')
            
            return {
                'message': 'Contraseña actualizada exitosamente'
            }, 200
            
        except Exception as e:
            print(f'❌ Error en change_password: {e}')
            return {
                'message': 'Error cambiando contraseña',
                'error': str(e)
            }, 500
    
    @staticmethod
    def _validate_profile_data(data, current_user):
        """
        Validar datos del perfil
        
        Args:
            data (dict): Datos a validar
            current_user (User): Usuario actual
            
        Returns:
            dict: Resultado de validación
        """
        # Lista de campos válidos para actualizar
        allowed_fields = [
            'fullName', 'email', 'username', 'profilePicture', 
            'gender', 'address', 'phoneNumber'
        ]
        
        # Verificar que no se envíen campos no permitidos
        invalid_fields = [field for field in data.keys() if field not in allowed_fields]
        if invalid_fields:
            return {
                'has_errors': True,
                'message': f'Campos no permitidos: {", ".join(invalid_fields)}'
            }
        
        # Al menos un campo debe ser enviado
        if not any(field in data for field in allowed_fields):
            return {
                'has_errors': True,
                'message': 'Debe proporcionar al menos un campo para actualizar'
            }
        
        return {'has_errors': False, 'message': 'Validación exitosa'}
