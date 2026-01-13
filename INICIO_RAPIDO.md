# Guía de Inicio Rápido - El Rincón del Pescador

## 🚀 Primeros Pasos

### 1. Instalar Python
Si no tienes Python instalado:
- Descarga desde: https://www.python.org/downloads/
- **IMPORTANTE**: Marca "Add Python to PATH" durante la instalación

### 2. Ejecutar Setup
```bash
setup.bat
```
Este script automáticamente:
- Crea el entorno virtual
- Instala dependencias
- Ejecuta migraciones
- Ofrece cargar datos de ejemplo

### 3. Crear Superusuario
```bash
venv\Scripts\activate
python manage.py createsuperuser
```
Ingresa:
- Username (ej: admin)
- Email (opcional)
- Password (mínimo 8 caracteres)

### 4. Iniciar Servidor
```bash
start.bat
```
O manualmente:
```bash
venv\Scripts\activate
python manage.py runserver
```

### 5. Acceder a la Aplicación
- **Sitio web**: http://localhost:8000/
- **Panel admin**: http://localhost:8000/admin/

## 📱 Instalar como PWA

### En el Celular
1. Abre http://localhost:8000/ en Chrome
2. Menú (⋮) → "Agregar a pantalla de inicio"
3. ¡Listo! Tendrás el ícono en tu pantalla

### En la PC
1. Abre http://localhost:8000/ en Chrome/Edge
2. Busca el ícono ➕ en la barra de direcciones
3. Clic en "Instalar"

## 🎣 Datos de Ejemplo

Si cargaste los datos de ejemplo, verás:
- 5 categorías de productos
- 10 productos de pesca
- Productos destacados en la página principal

## ❓ Solución de Problemas

### Python no encontrado
- Reinstala Python marcando "Add to PATH"
- O usa la ruta completa: `C:\Python3X\python.exe`

### Error en migraciones
```bash
python manage.py migrate --run-syncdb
```

### Puerto 8000 ocupado
```bash
python manage.py runserver 8080
```
Luego accede a http://localhost:8080/

## 📚 Más Información

Ver README.md para documentación completa.
