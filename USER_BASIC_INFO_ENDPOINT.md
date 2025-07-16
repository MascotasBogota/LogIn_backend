# 📋 Endpoint: Obtener Información Básica de Usuario

## 🎯 Descripción
Nuevo endpoint que permite obtener información básica de cualquier usuario por su ID, sin necesidad de autenticación JWT.

## 📡 Endpoint
```
GET /api/profile/user/{user_id}
```

## 🔑 Parámetros
- **user_id** (string, requerido): ID del usuario a consultar

## 🔒 Autenticación
- **No requiere autenticación JWT**
- Es un endpoint público

## 📊 Respuesta Exitosa (200)
```json
{
  "message": "Información del usuario obtenida exitosamente",
  "user": {
    "id": "64f7b1c2d4e5f6a7b8c9d0e1",
    "full_name": "Juan Carlos Pérez",
    "username": "juanperez",
    "email": "juan@ejemplo.com",
    "profile_picture": "/static/uploads/profile_pictures/user_123.jpg",
    "reputation": 150
  }
}
```

## ❌ Respuesta de Error (404)
```json
{
  "message": "Usuario no encontrado"
}
```

## ❌ Respuesta de Error (500)
```json
{
  "message": "Error interno del servidor"
}
```

## 🚀 Ejemplos de Uso

### JavaScript/Fetch
```javascript
const getUserInfo = async (userId) => {
  try {
    const response = await fetch(`/api/profile/user/${userId}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    });
    
    const data = await response.json();
    
    if (response.ok) {
      return data.user;
    } else {
      throw new Error(data.message);
    }
  } catch (error) {
    console.error('Error obteniendo información del usuario:', error);
    throw error;
  }
};

// Uso
getUserInfo('64f7b1c2d4e5f6a7b8c9d0e1')
  .then(user => {
    console.log('Usuario:', user);
  })
  .catch(error => {
    console.error('Error:', error.message);
  });
```

### Python/Requests
```python
import requests

def get_user_info(user_id):
    """Obtener información básica de un usuario"""
    try:
        response = requests.get(f'http://localhost:5000/api/profile/user/{user_id}')
        
        if response.status_code == 200:
            return response.json()['user']
        else:
            raise Exception(response.json()['message'])
            
    except requests.exceptions.RequestException as e:
        raise Exception(f'Error de conexión: {str(e)}')

# Uso
try:
    user_info = get_user_info('64f7b1c2d4e5f6a7b8c9d0e1')
    print(f"Usuario: {user_info['full_name']}")
    print(f"Email: {user_info['email']}")
    print(f"Reputación: {user_info['reputation']}")
except Exception as e:
    print(f"Error: {e}")
```

### cURL
```bash
# Obtener información básica de un usuario
curl -X GET "http://localhost:5000/api/profile/user/64f7b1c2d4e5f6a7b8c9d0e1" \
  -H "Content-Type: application/json"
```

## 🔧 Casos de Uso

### 1. **Mostrar Información de Usuario en Reportes**
```javascript
// Cuando se muestra un reporte, obtener info del usuario que lo creó
const displayReport = async (report) => {
  const userInfo = await getUserInfo(report.user_id);
  
  document.getElementById('report-author').innerHTML = `
    <div class="user-info">
      <img src="${userInfo.profile_picture || '/default-avatar.png'}" alt="Avatar">
      <div>
        <h4>${userInfo.full_name}</h4>
        <p>@${userInfo.username || 'Sin username'}</p>
        <span class="reputation">⭐ ${userInfo.reputation} puntos</span>
      </div>
    </div>
  `;
};
```

### 2. **Validar Existencia de Usuario**
```javascript
const validateUser = async (userId) => {
  try {
    const userInfo = await getUserInfo(userId);
    return { exists: true, user: userInfo };
  } catch (error) {
    return { exists: false, error: error.message };
  }
};
```

### 3. **Mostrar Lista de Usuarios**
```javascript
const displayUserList = async (userIds) => {
  const users = await Promise.all(
    userIds.map(async (id) => {
      try {
        return await getUserInfo(id);
      } catch (error) {
        return null; // Usuario no encontrado
      }
    })
  );
  
  const validUsers = users.filter(user => user !== null);
  // Mostrar lista de usuarios válidos
};
```

## 📋 Campos Devueltos

| Campo | Tipo | Descripción | Ejemplo |
|-------|------|-------------|---------|
| `id` | string | ID único del usuario | `"64f7b1c2d4e5f6a7b8c9d0e1"` |
| `full_name` | string | Nombre completo | `"Juan Carlos Pérez"` |
| `username` | string \| null | Nombre de usuario | `"juanperez"` |
| `email` | string | Correo electrónico | `"juan@ejemplo.com"` |
| `profile_picture` | string \| null | URL de foto de perfil | `"/static/uploads/profile.jpg"` |
| `reputation` | number | Reputación del usuario | `150` |

## 🔒 Seguridad

### ✅ **Información Segura**
- No se incluye la contraseña
- No se incluyen campos sensibles como teléfono o dirección
- Solo información básica y pública

### ✅ **Sin Autenticación**
- No requiere JWT token
- Endpoint público
- Ideal para mostrar información básica en interfaces

## 🚀 Integración con Otros Servicios

### Servicio de Reportes
```javascript
// Al crear un reporte, validar que el usuario existe
const createReport = async (reportData) => {
  const userValidation = await validateUser(reportData.user_id);
  
  if (!userValidation.exists) {
    throw new Error('Usuario no válido');
  }
  
  // Proceder con la creación del reporte
  // e incluir información básica del usuario
  reportData.user_info = userValidation.user;
  
  return await submitReport(reportData);
};
```

### Servicio de Notificaciones
```javascript
// Al enviar notificación, obtener info del usuario
const sendNotification = async (userId, message) => {
  const userInfo = await getUserInfo(userId);
  
  const notification = {
    to: userInfo.email,
    subject: `Hola ${userInfo.full_name}`,
    message: message,
    user_reputation: userInfo.reputation
  };
  
  return await sendEmail(notification);
};
```

## 📊 Swagger/OpenAPI

El endpoint está documentado automáticamente en:
- **Swagger UI**: http://localhost:5000/docs/
- **Sección**: Profile Management
- **Operación**: `get_user_basic_info`

## 🧪 Testing

### Ejecutar Tests
```bash
# Ejecutar solo tests del profile controller
python -m pytest tests/test_profile_controller.py::TestProfileController::test_get_user_basic_info_success -v

# Ejecutar todos los tests nuevos
python -m pytest tests/test_profile_controller.py -k "test_get_user_basic_info" -v
```

### Tests Incluidos
- ✅ `test_get_user_basic_info_success`: Usuario encontrado exitosamente
- ✅ `test_get_user_basic_info_not_found`: Usuario no encontrado
- ✅ `test_get_user_basic_info_with_null_values`: Manejo de valores null

## 🎯 Ventajas del Endpoint

### ✅ **Rendimiento**
- Consulta directa por ID (muy rápida)
- Solo campos esenciales
- No requiere autenticación (menos overhead)

### ✅ **Usabilidad**
- Fácil de usar desde frontend
- Perfecto para mostrar información de usuarios
- Integración simple con otros servicios

### ✅ **Seguridad**
- Solo información pública
- No expone datos sensibles
- Manejo de errores robusto

---

💡 **Este endpoint es perfecto para obtener información básica de usuarios sin necesidad de autenticación, ideal para mostrar detalles de usuarios en reportes, comentarios o listados públicos.**
