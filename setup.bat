@echo off
echo ============================================
echo Setup de El Rincon del Pescador
echo ============================================
echo.

REM Verificar si Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado.
    echo.
    echo Por favor instala Python desde: https://www.python.org/downloads/
    echo Asegurate de marcar "Add Python to PATH" durante la instalacion.
    echo.
    pause
    exit /b 1
)

echo [1/6] Python encontrado
python --version
echo.

REM Crear entorno virtual
echo [2/6] Creando entorno virtual...
if not exist venv (
    python -m venv venv
    echo Entorno virtual creado exitosamente
) else (
    echo Entorno virtual ya existe
)
echo.

REM Activar entorno virtual
echo [3/6] Activando entorno virtual...
call venv\Scripts\activate.bat
echo.

REM Instalar dependencias
echo [4/6] Instalando dependencias...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.

REM Ejecutar migraciones
echo [5/6] Ejecutando migraciones de base de datos...
python manage.py makemigrations
python manage.py migrate
echo.

REM Cargar datos de ejemplo (opcional)
echo [6/6] Deseas cargar datos de ejemplo? (S/N)
set /p LOAD_DATA="> "
if /i "%LOAD_DATA%"=="S" (
    if exist tienda\fixtures\sample_data.json (
        python manage.py loaddata tienda/fixtures/sample_data.json
        echo Datos de ejemplo cargados exitosamente
    ) else (
        echo No se encontro el archivo de datos de ejemplo
    )
)
echo.

echo ============================================
echo Setup completado exitosamente!
echo ============================================
echo.
echo Ahora necesitas crear un superusuario para acceder al panel de admin:
echo   python manage.py createsuperuser
echo.
echo Para iniciar el servidor de desarrollo:
echo   python manage.py runserver
echo.
echo Luego accede a:
echo   - Sitio web: http://localhost:8000/
echo   - Panel admin: http://localhost:8000/admin/
echo.
pause
