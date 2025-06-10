"""
Servicio para envío de emails
"""
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import current_app

class EmailService:
    """Servicio para envío de emails"""
    
    @staticmethod
    def get_smtp_config():
        """Obtener configuración SMTP desde variables de entorno"""
        return {
            'smtp_server': os.getenv('SMTP_SERVER', 'smtp.gmail.com'),
            'smtp_port': int(os.getenv('SMTP_PORT', 587)),
            'smtp_username': os.getenv('SMTP_USERNAME'),
            'smtp_password': os.getenv('SMTP_PASSWORD'),
            'from_email': os.getenv('FROM_EMAIL', os.getenv('SMTP_USERNAME'))
        }
    
    @staticmethod
    def send_email(to_email, subject, html_content, text_content=None):
        """
        Enviar email con contenido HTML y texto plano
        
        Args:
            to_email (str): Email del destinatario
            subject (str): Asunto del email
            html_content (str): Contenido HTML del email
            text_content (str): Contenido en texto plano (opcional)
        
        Returns:
            bool: True si se envió exitosamente, False en caso contrario
        """
        try:
            config = EmailService.get_smtp_config()
            
            # Verificar configuración requerida
            if not config['smtp_username'] or not config['smtp_password']:
                print("❌ Configuración SMTP incompleta. Simulando envío de email...")
                print(f"📧 Email simulado a: {to_email}")
                print(f"📧 Asunto: {subject}")
                print(f"📧 Contenido: {text_content or html_content}")
                return True  # Simular éxito para desarrollo
            
            # Crear mensaje
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = config['from_email']
            message["To"] = to_email
            
            # Agregar contenido de texto plano
            if text_content:
                text_part = MIMEText(text_content, "plain")
                message.attach(text_part)
            
            # Agregar contenido HTML
            html_part = MIMEText(html_content, "html")
            message.attach(html_part)
            
            # Conectar y enviar
            with smtplib.SMTP(config['smtp_server'], config['smtp_port']) as server:
                server.starttls()
                server.login(config['smtp_username'], config['smtp_password'])
                server.send_message(message)
            
            print(f"✅ Email enviado exitosamente a: {to_email}")
            return True
            
        except Exception as e:
            print(f"❌ Error enviando email: {e}")
            return False
    
    @staticmethod
    def send_password_reset_email(user_email, user_name, reset_token):
        """
        Enviar email de restablecimiento de contraseña
        
        Args:
            user_email (str): Email del usuario
            user_name (str): Nombre del usuario
            reset_token (str): Token de restablecimiento
        
        Returns:
            bool: True si se envió exitosamente
        """
        # URL base del frontend (configurable)
        frontend_url = os.getenv('FRONTEND_URL', 'http://localhost:3000')
        reset_url = f"{frontend_url}/reset-password?token={reset_token}"
        
        subject = "Restablece tu contraseña - Mascotas App"
        
        # Contenido HTML del email
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Restablece tu contraseña</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    background-color: #4CAF50;
                    color: white;
                    padding: 20px;
                    text-align: center;
                    border-radius: 8px 8px 0 0;
                }}
                .content {{
                    background-color: #f9f9f9;
                    padding: 30px;
                    border-radius: 0 0 8px 8px;
                }}
                .button {{
                    display: inline-block;
                    background-color: #4CAF50;
                    color: white;
                    padding: 12px 24px;
                    text-decoration: none;
                    border-radius: 4px;
                    margin: 20px 0;
                }}
                .footer {{
                    margin-top: 20px;
                    padding-top: 20px;
                    border-top: 1px solid #ddd;
                    font-size: 14px;
                    color: #666;
                }}
                .warning {{
                    background-color: #fff3cd;
                    border: 1px solid #ffeaa7;
                    padding: 15px;
                    border-radius: 4px;
                    margin: 20px 0;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🐾 Mascotas App</h1>
                <h2>Restablecimiento de Contraseña</h2>
            </div>
            
            <div class="content">
                <p>Hola <strong>{user_name}</strong>,</p>
                
                <p>Recibimos una solicitud para restablecer la contraseña de tu cuenta en Mascotas App.</p>
                
                <p>Haz clic en el siguiente botón para crear una nueva contraseña:</p>
                
                <div style="text-align: center;">
                    <a href="{reset_url}" class="button">Restablecer Contraseña</a>
                </div>
                
                <p>O copia y pega este enlace en tu navegador:</p>
                <p style="word-break: break-all; background-color: #f0f0f0; padding: 10px; border-radius: 4px;">
                    {reset_url}
                </p>
                
                <div class="warning">
                    <strong>⚠️ Importante:</strong>
                    <ul>
                        <li>Este enlace expira en <strong>1 hora</strong></li>
                        <li>Solo puede ser usado una vez</li>
                        <li>Si no solicitaste este cambio, ignora este email</li>
                    </ul>
                </div>
                
                <div class="footer">
                    <p>Si tienes problemas con el enlace, contacta nuestro soporte.</p>
                    <p>Gracias,<br>El equipo de Mascotas App</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Contenido en texto plano (fallback)
        text_content = f"""
        Hola {user_name},

        Recibimos una solicitud para restablecer la contraseña de tu cuenta en Mascotas App.

        Usa este enlace para crear una nueva contraseña:
        {reset_url}

        IMPORTANTE:
        - Este enlace expira en 1 hora
        - Solo puede ser usado una vez
        - Si no solicitaste este cambio, ignora este email

        Gracias,
        El equipo de Mascotas App
        """
        
        return EmailService.send_email(user_email, subject, html_content, text_content)
