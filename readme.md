# Proyecto: Blog en Django
<!-- Este readme fue creado por Juan amaya y Andres Urango -->
## Tabla de contenido
* [Descripción del proyecto](#descripcion-del-proyecto)  
* [Instalación](#instrucciones-para-instalar-y-ejecutar-el-proyecto)
* [Error al instalar entorno virtual](#si-encuentras-problemas-con-la-ejecucion-de-scripts-pssecurityexception-sigue-estos-pasos)
 

## Descripcion del Proyecto
Este es un proyecto de un blog básico desarrollado con el framework **Django**, con el objetivo de poner en practica conocimientos sobre modelos, vistas, plantillas y formularios. El blog permite a los usuarios consultar todas las punlicaciones, crear, visualizar e interactuar con publicaciones de manera sencilla.

### Funcionalidades:
- **Pagina de inicio**: Muestra una lista con todas las publicaciones, incluyendo el título, el contenido y la fecha de publicación.
- **Vista detallada**: Muestra el contenido completo de una publicación al hacer clic en el título o en el botón "Leer Más".  
- **Formulario de creacion**: Permite crear nuevas publicaciones fácilmente desde la web.
- **Navegación**: Enlaces intuitivos para navegar entre las secciones principales del blog.  

## Instrucciones para Instalar y Ejecutar el Proyecto

1. **Clonar el repositorio**:
```bash
git clone https://github.com/AndresUrango10/Blog_con_Django.git
```

Navega al directorio del proyecto:

 cd MyBlogAJ

## Crea y activa un entorno virtual:

2. **Crear un entorno virtual en Windows**
```bash
     python -m venv env  # En (Linux/Mac) usa  `python3 -m venv env` 
```
3. **Activa el entorno virtual en Windows**
```bash 
     env\Scripts\activate # En (Linux/Mac) usa `source env/bin/activate`
```
4. **Si no presentas ningun problema realiza la instalacion de Django en tu entorno virtual**
```bash 
     pip install django
```

## Si encuentras problemas con la ejecucion de scripts (PSSecurityException), sigue estos pasos:

De manera predeterminada, PowerShell bloquea la ejecución de scripts como medida de seguridad. Este es el error PSSecurityException que indica que no tienes permiso para ejecutar el script Activate.ps1 que intenta activar el entorno virtual de Python.

Para solucionarlo, puedes cambiar la política de ejecución de PowerShell temporalmente a una menos restrictiva con los siguientes pasos:

1. **Abre PowerShell como administrador**:
- Haz clic en el botón de inicio de Windows.
- Busca "PowerShell".
- Haz clic derecho en "Windows PowerShell" y selecciona "Ejecutar como administrador".
2. **Cambia la política de ejecución**:
Ejecuta este comando en la ventana de PowerShell:
```bash
    Set-ExecutionPolicy RemoteSigned
```

- ?  Esto permitirá que se ejecuten scripts locales que no están firmados, pero requerirá que los scripts descargados de internet estén firmados por un editor de confianza.
3. **Confirma el cambio:**
Cuando se te pregunte si deseas cambiar la política de ejecución, escribe **Y**, u **O** y presiona Enter.

4. **Reintentar activar el entorno virtual:**

Vuelve a la terminal en tu proyecto de Django y ejecuta:
```bash 
     env\Scripts\activate # En (Linux/Mac) usa `source env/bin/activate`
```
- **Una vez activado, verás que el nombre del entorno virtual aparece al principio de la línea de comandos, algo como (env).**
5. **Realiza la instalcion de Django en tu entorno virtual**
```bash 
     pip install django
```
6. **(Opcional) si quieres verificar que esta bien instalado**
```bash
    django-admin --version
```
7. **Realiza las migraciones**
```bash
    python manage.py migrate
```
8. **Iniciar el servidor**
```bash 
    python manage.py runserver
```
Cuando ejecutes este comando, deberías ver una salida similar a esta en la terminal:
Starting development server at http://127.0.0.1:8000/ Acceda a el.

9. **(Opcional) si quieres crearte un super usuario realiza el siguiente comando**
```bash 
    python manage.py createsuperuser
```
