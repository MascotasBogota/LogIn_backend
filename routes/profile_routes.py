"""
Rutas para gestión de perfil de usuario
"""
from flask import Blueprint, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import jwt
from functools import wraps
from controllers.profile_controller import ProfileController
from controllers.reputation_controller import ReputationController
import os
from utils.serialization import serialize_response

# Crear blueprint para rutas de perfil
profile_bp = Blueprint('profile', __name__)

# Configurar rate limiter
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="memory://",
    default_limits=["200 per day", "50 per hour"]
)

def token_required(f):
    """
    Decorador para verificar token JWT en las rutas protegidas
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        # JWT se puede enviar en el header Authorization
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                token = auth_header.split(" ")[1]  # "Bearer <token>"
            except IndexError:
                return jsonify({'message': 'Formato de token inválido'}), 401
        
        if not token:
            return jsonify({'message': 'Token requerido'}), 401
        
        try:
            # Decodificar token
            secret_key = os.getenv('JWT_SECRET', 'mascotas_secret_key')
            data = jwt.decode(token, secret_key, algorithms=['HS256'])
            current_user_id = data['userId']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token inválido'}), 401
        
        return f(current_user_id, *args, **kwargs)
    
    return decorated

@profile_bp.route('/', methods=['GET'])
@token_required
def get_profile(current_user_id):
    """
    Obtener información del perfil del usuario autenticado
    
    Headers:
        Authorization: Bearer <jwt_token>
    """
    try:
        # Llamar al controlador
        response_data, status_code = ProfileController.get_profile(current_user_id)
        return jsonify(response_data), status_code
        
    except Exception as e:
        return jsonify({
            'message': 'Error obteniendo perfil',
            'error': str(e)
        }), 500

@profile_bp.route('/', methods=['PUT'])
@token_required
def update_profile(current_user_id):
    """
    Actualizar información del perfil del usuario autenticado
    
    Headers:
        Authorization: Bearer <jwt_token>
    
    Expected JSON:
    {
        "full_name": "Nuevo Nombre",
        "email": "nuevo@email.com",
        "username": "nuevo_username",
        "profilePicture": "url_to_image",
        "gender": "male|female|other|prefer_not_to_say",
        "address": "Nueva dirección",
        "phoneNumber": "+1234567890"
    }
    
    Nota: Todos los campos son opcionales. Solo se actualizarán los campos enviados.
    """
    try:
        # Obtener datos JSON del request
        request_data = request.get_json()
        
        if not request_data:
            return jsonify({'message': 'No se enviaron datos'}), 400
        
        # Llamar al controlador
        response_data, status_code = ProfileController.update_profile(current_user_id, request_data)
        return jsonify(response_data), status_code
        
    except Exception as e:
        return jsonify({
            'message': 'Error actualizando perfil',
            'error': str(e)
        }), 500

@profile_bp.route('/change-password', methods=['PUT'])
@token_required
def change_password(current_user_id):
    """
    Cambiar contraseña del usuario autenticado
    
    Headers:
        Authorization: Bearer <jwt_token>
    
    Expected JSON:
    {
        "currentPassword": "contraseña_actual",
        "newPassword": "nueva_contraseña"
    }
    """
    try:
        # Obtener datos JSON del request
        request_data = request.get_json()
        
        if not request_data:
            return jsonify({'message': 'No se enviaron datos'}), 400
        
        # Llamar al controlador
        response_data, status_code = ProfileController.change_password(current_user_id, request_data)
        return jsonify(response_data), status_code
        
    except Exception as e:
        return jsonify({
            'message': 'Error cambiando contraseña',
            'error': str(e)
        }), 500

@profile_bp.route('/upload-picture', methods=['POST'])
@token_required
def upload_profile_picture(current_user_id):
    """
    Subir foto de perfil
    
    Headers:
        Authorization: Bearer <jwt_token>
    
    Form Data:
        file: imagen de perfil (png, jpg, jpeg, gif)
    """
    try:
        # Verificar que se envió un archivo
        if 'file' not in request.files:
            return jsonify({'message': 'No se envió ningún archivo'}), 400
        
        file = request.files['file']
        
        # Llamar al controlador para procesar el archivo
        response_data, status_code = ProfileController.upload_profile_picture(current_user_id, file)
        return jsonify(response_data), status_code
        
    except Exception as e:
        return jsonify({
            'message': 'Error subiendo foto de perfil',
            'error': str(e)
        }), 500

@profile_bp.route('/<user_id_to_update>/reputation', methods=['PATCH'])
@token_required
def update_user_reputation(current_user_id,user_id_to_update):
    """
    Actualizar la reputación de un usuario.
    Solo un administrador o el propio usuario puede actualizar su reputación.
    
    Headers:
        Authorization: Bearer <jwt_token>
    
    Expected JSON:
    {
        "reputation_delta": 5
    }
    """
    try:
        token = request.headers.get('Authorization')
        print(f"🆔 Token recibido: {token}")
        request_data = request.get_json()
        if not request_data or 'reputation_delta' not in request_data:
            return jsonify({'message': 'Payload inválido. Se espera {"reputation_delta": int}'}), 400

        reputation_delta = request_data['reputation_delta']
        if not isinstance(reputation_delta, int):
            return jsonify({'message': 'reputation_delta debe ser un entero'}), 400
        
        print(f"Updating reputation for user {user_id_to_update} by {reputation_delta}")
        response_data, status_code = ReputationController.update_reputation(user_id_to_update, reputation_delta)
        print(f"🆗 Reputación actualizada: {response_data}, status code {status_code}")
        return response_data, status_code

    except Exception as e:
        print(f"❌ Error al actualizar la reputación: {str(e)}")
        return jsonify({
            'message': 'Error actualizando la reputación',
            'error': str(e)
        }), 500

@profile_bp.route('/user/<user_id>', methods=['GET'])
def get_user_basic_info(user_id):
    """
    Obtener información básica de un usuario por ID
    
    URL Parameters:
        user_id: ID del usuario a consultar
    
    Response:
    {
        "message": "Información del usuario obtenida exitosamente",
        "user": {
            "id": "user_id",
            "full_name": "Juan Pérez",
            "username": "juanperez",
            "email": "juan@ejemplo.com",
            "profile_picture": "/static/uploads/profile.jpg",
            "reputation": 150
        }
    }
    """
    try:
        response_data, status_code = ProfileController.get_user_basic_info(user_id)
        return jsonify(response_data), status_code
        
    except Exception as e:
        return jsonify({
            'message': 'Error obteniendo información del usuario',
            'error': str(e)
        }), 500
