@echo off
echo ============================================
echo El Rincon del Pescador - Inicio Rapido
echo ============================================
echo.

REM Verificar si el entorno virtual existe
if not exist venv (
    echo ERROR: El entorno virtual no existe.
    echo.
    echo Por favor ejecuta primero: setup.bat
    echo.
    pause
    exit /b 1
)

REM Activar entorno virtual
call venv\Scripts\activate.bat

echo Iniciando servidor de desarrollo...
echo.
echo La aplicacion estara disponible en:
echo   - Sitio web: http://localhost:8000/
echo   - Panel admin: http://localhost:8000/admin/
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

REM Iniciar servidor
python manage.py runserver 0.0.0.0:8000
