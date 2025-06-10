"""
Aplicación principal Flask para Mascotas App
"""
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import os

from config.database import init_db
from routes.user_routes import user_bp
from routes.password_reset_routes import password_reset_bp
from routes.profile_routes import profile_bp

# Cargar variables de entorno
load_dotenv()

def create_app():
    """Factory function para crear la aplicación Flask"""
    app = Flask(__name__)
    
    # Configuración
    app.config['SECRET_KEY'] = os.getenv('JWT_SECRET', 'mascotas_secret_key')
    app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost:27017/mascotas-app')
    
    # Configuración para archivos subidos
    app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB max file size
    
    # Configurar CORS
    CORS(app, origins=['http://localhost:5173', 'http://localhost:3000'])
    
    # Inicializar base de datos
    init_db(app)
    
    # Crear carpeta de uploads si no existe
    upload_folder = 'uploads'
    os.makedirs(upload_folder, exist_ok=True)
    
    # Registrar blueprints (rutas)
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(password_reset_bp, url_prefix='/api/auth')
    app.register_blueprint(profile_bp, url_prefix='/api/profile')
    
    # Ruta para servir archivos estáticos (imágenes subidas)
    @app.route('/static/uploads/<path:filename>')
    def uploaded_file(filename):
        """Servir archivos subidos"""
        return send_from_directory('uploads', filename)
    
    # Ruta de prueba raíz
    @app.route('/')
    def home():
        return jsonify({'message': 'Mascotas App API is running 🐾'})
    
    # Ruta de prueba para /api
    @app.route('/api')
    def api_test():
        return jsonify({'message': 'API endpoint working ✅'})
    
    # Manejador de errores 404
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'message': f'Route not found'}), 404
    
    # Manejador de errores 500
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'message': 'Internal server error'}), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.getenv('PORT', 5000))
    
    print(f'🚀 Server running on port {port}')
    print(f'📡 API available at: http://localhost:{port}/api')
    
    app.run(host='0.0.0.0', port=port, debug=True)
