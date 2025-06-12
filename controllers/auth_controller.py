"""
Controlador de autenticación que integra UserController y PasswordResetController
"""
from .user_controller import UserController
from .password_reset_controller import PasswordResetController

class AuthController:
    """Controlador unificado para todas las operaciones de autenticación"""
    
    @staticmethod
    async def register(data):
        """
        Registrar nuevo usuario
        
        Args:
            data (dict): Datos de registro del usuario
            
        Returns:
            tuple: (response_data, status_code)
        """
        return await UserController.register_user(data)
    
    @staticmethod
    def login(data):
        """
        Iniciar sesión de usuario
        
        Args:
            data (dict): Credenciales de login
            
        Returns:
            tuple: (response_data, status_code)
        """
        return UserController.login_user(data)
    
    @staticmethod
    def forgot_password(data):
        """
        Solicitar restablecimiento de contraseña
        
        Args:
            data (dict): Datos con email del usuario
            
        Returns:
            tuple: (response_data, status_code)
        """
        return PasswordResetController.request_password_reset(data)
    
    @staticmethod
    def verify_reset_token(data):
        """
        Verificar token de restablecimiento
        
        Args:
            data (dict): Datos con token a verificar
            
        Returns:
            tuple: (response_data, status_code)
        """
        return PasswordResetController.verify_reset_token(data)
    
    @staticmethod
    def reset_password(data):
        """
        Restablecer contraseña con token válido
        
        Args:
            data (dict): Datos con token y nueva contraseña
            
        Returns:
            tuple: (response_data, status_code)
        """
        return PasswordResetController.reset_password(data)
