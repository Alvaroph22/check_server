# Proyecto de Verificación de Estado del Servidor

Este proyecto verifica el estado de un servidor web y envía una notificación por correo electrónico si el servidor no responde correctamente.

## Requisitos

- Python 3.x
- pip (gestor de paquetes de Python)

## Instalación

1. Clona este repositorio en tu máquina local.
2. Navega al directorio del proyecto.
3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Crea un archivo `.env` en el directorio del proyecto con el siguiente contenido:

    ```plaintext
    EMAIL_PASSWORD=tu_contraseña
    ```

## Uso

1. Ejecuta el script:

    ```bash
    python check_server_status.py
    ```

2. Introduce la URL del servidor que deseas monitorear.

## Contribuciones

Si deseas contribuir a este proyecto, por favor crea una rama nueva, realiza tus cambios y envía un pull request.
