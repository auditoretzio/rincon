# Guía de Uso con Ngrok

Esta guía explica cómo exponer tu servidor de desarrollo local de Django a internet utilizando **ngrok**, permitiendo que otras personas (como colaboradores en otras redes) accedan a tu sitio web, incluyendo el panel de administración.

## Prerrequisitos

1.  **Tener el servidor de Django corriendo**:
    Asegúrate de que tu entorno virtual esté activado y tu servidor esté en ejecución.
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```
    *Nota: Usamos `0.0.0.0:8000` para asegurarnos de que escuche en todas las interfaces, aunque `127.0.0.1:8000` (el defecto) suele funcionar bien con ngrok.*


2.  **Tener Ngrok instalado**:
    *   **Opción recomendada (Windows):** Abre una terminal y ejecuta:
        ```powershell
        winget install Ngrok.Ngrok
        ```
        (Luego reinicia tu terminal para que reconozca el comando).
    *   **Opción manual:** Descárgalo e instálalo desde [ngrok.com](https://ngrok.com/download).
    
    Debes crear una cuenta gratuita y configurar tu authtoken una sola vez.

## Exponiendo el Sitio

1.  Abre una **nueva terminal** (mantén la terminal de Django corriendo).
2.  Ejecuta el siguiente comando:
    ```bash
    ngrok http 8000
    ```

3.  Verás una pantalla como esta:
    ```text
    ngrok                                                                     (Ctrl+C to quit)

    Session Status                online
    Account                       Tu Nombre (Plan: Free)
    Version                       3.x.x
    Region                        United States (us)
    Forwarding                    https://xxxx-xxxx.ngrok-free.app -> http://localhost:8000
    ```

4.  **Copia la dirección HTTPS** de "Forwarding" (ejemplo: `https://xxxx-xxxx.ngrok-free.app`).
5.  Comparte ese enlace con la otra persona.

## Notas Importantes

-   **Seguridad**: Hemos configurado `CSRF_TRUSTED_ORIGINS` en `settings.py` para permitir que los formularios (como el login de administrador) funcionen correctamente a través de esta dirección segura.
-   **Duración**: En la versión gratuita de ngrok, la URL cambia cada vez que reinicias el comando `ngrok`.
-   **Sitio de Advertencia de Ngrok**: La primera vez que alguien visite el enlace, ngrok mostrará una página de advertencia de seguridad. Solo deben hacer clic en "Visit Site".
