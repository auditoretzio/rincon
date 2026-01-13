# Proyecto Django: El Rincón del Pescador 🎣

Tienda online de artículos de pesca construida con Django y convertida en **Progressive Web App (PWA)**.

## 🚀 Características

### Funcionalidades de la Tienda
- **Gestión de productos**: Administra artículos de pesca desde el panel de Django
- **Categorías**: Organiza productos por categorías (Cañas, Carretes, Señuelos, etc.)
- **Imágenes**: Sube imágenes para cada producto
- **Stock**: Control de inventario en tiempo real
- **Productos destacados**: Marca productos para mostrar en la página principal
- **Diseño responsive**: Funciona perfectamente en dispositivos móviles y escritorio

### PWA (Progressive Web App) ✨
- 📱 **Instalable**: Instala la app en tu dispositivo móvil o escritorio
- 🔌 **Modo Offline**: Funciona sin conexión gracias al Service Worker
- ⚡ **Carga Rápida**: Sistema de caché inteligente para mejor rendimiento
- 🎨 **Iconos Personalizados**: Diseño profesional con temática de pesca
- 🌊 **Experiencia Nativa**: Se comporta como una app nativa en dispositivos móviles

## 📦 Instalación Rápida

### Opción 1: Script Automático (Recomendado)

1. Asegúrate de tener Python 3.8+ instalado
2. Ejecuta el script de setup:
```bash
setup.bat
```

El script automáticamente:
- ✅ Verifica la instalación de Python
- ✅ Crea un entorno virtual
- ✅ Instala todas las dependencias
- ✅ Ejecuta las migraciones de base de datos
- ✅ Ofrece cargar datos de ejemplo

### Opción 2: Instalación Manual

1. **Crear un entorno virtual:**
```bash
python -m venv venv
```

2. **Activar el entorno virtual:**
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Ejecutar migraciones:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Cargar datos de ejemplo (opcional):**
```bash
python manage.py loaddata tienda/fixtures/sample_data.json
```

6. **Crear superusuario para el panel de administración:**
```bash
python manage.py createsuperuser
```

7. **Ejecutar el servidor de desarrollo:**
```bash
python manage.py runserver
```

8. **Acceder a la aplicación:**
- Sitio web: http://localhost:8000/
- Panel de administración: http://localhost:8000/admin/

## 📱 Instalar como PWA

### En Dispositivos Móviles (Android/iOS)
1. Abre http://localhost:8000/ en Chrome/Safari
2. Toca el menú del navegador (⋮ o ⋯)
3. Selecciona "Agregar a pantalla de inicio" o "Instalar app"
4. ¡Listo! La app aparecerá en tu pantalla de inicio

### En Escritorio (Chrome/Edge)
1. Abre http://localhost:8000/ en Chrome o Edge
2. Busca el ícono de instalación (➕) en la barra de direcciones
3. Haz clic en "Instalar"
4. La app se abrirá en su propia ventana

## 🗂️ Estructura del Proyecto

```
el_rincon_del_pescador/
├── manage.py
├── setup.bat                      # Script de instalación automática
├── requirements.txt
├── rincon_pescador/              # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── tienda/                       # Aplicación de la tienda
    ├── models.py                 # Modelos de datos
    ├── admin.py                  # Configuración del admin
    ├── views.py                  # Vistas
    ├── urls.py                   # URLs
    ├── fixtures/                 # Datos de ejemplo
    │   └── sample_data.json
    ├── templates/                # Plantillas HTML
    │   └── tienda/
    │       ├── base.html
    │       ├── index.html
    │       ├── categoria.html
    │       └── producto_detalle.html
    └── static/                   # Archivos estáticos
        └── tienda/
            ├── css/
            │   └── styles.css
            ├── icons/            # Iconos PWA
            │   ├── icon-192x192.png
            │   └── icon-512x512.png
            ├── manifest.json     # Manifiesto PWA
            └── sw.js            # Service Worker
```

## 🎨 Uso del Panel de Administración

1. Accede a http://localhost:8000/admin/
2. Inicia sesión con el superusuario creado
3. Gestiona categorías y productos desde el panel
4. Los cambios se reflejarán automáticamente en el sitio web

### Datos de Ejemplo Incluidos
Si cargaste los datos de ejemplo, encontrarás:
- 5 categorías de productos
- 10 productos de pesca variados
- Productos marcados como destacados
- Stock y precios configurados

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 4.2+
- **Base de Datos**: SQLite (desarrollo)
- **Frontend**: HTML5, CSS3, JavaScript
- **PWA**: Service Worker, Web App Manifest
- **Imágenes**: Pillow para procesamiento
- **Fuentes**: Google Fonts (Outfit)

## 🌐 Despliegue en Producción

Para desplegar en producción:

1. Configura las variables de entorno en `settings.py`
2. Cambia `DEBUG = False`
3. Configura `ALLOWED_HOSTS`
4. Usa una base de datos robusta (PostgreSQL recomendado)
5. Configura archivos estáticos con `collectstatic`
6. Usa un servidor WSGI (Gunicorn + Nginx)

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para sugerencias y mejoras.

---

**Desarrollado con ❤️ para pescadores apasionados**
