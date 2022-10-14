# Proyecto Backend: Ecommerce de Celulares

## Requisitos de la aplicación
1. Tener instalado un editor de texto como Visual Studio Code
2. Tener instalado Python
3. Tener instalado Postman
## Declaración de variables de entorno
- Crear un archivo .env
> FLASK_RUN_HOST=127.0.0.1   
> FLASK_RUN_PORT=5000  
> FLASK_DEBUG=true  
> DB_URI=mysql://root:tupassword@localhost/basedatos
## Creación de entorno virtual con venv
- Para crear el entorno virtual se usa el comando:
```bash
   $ python -m venv entorno_proyecto
```
- Para activar el entorno virtual se usa el comando ("bin" en MAC y "Scripts" en Windows):
```bash
   $ source venv/bin/activate
```
```bash
   $ source venv/Scripts/activate
```
- Para desactivar el entorno virtual se usa el comando:
```bash
   $ deactivate
```
## Instalación de librerías
- Para instalar las librerías que usa el proyecto se usa el comando:
```bash
   $ pip install -r requirements.txt
```
## Migración de modelos a la Base de datos
- Para crear las tablas en la Base de datos se usan los siguientes comandos:
```bash
   $ flask db init
   $ flask db migrate -m "Initial migration"
   $ flask db upgrade
```
## Puesta en marcha del servidor
- Para levantar el servidor se usa el comando:
```bash
   $ flask run
```
