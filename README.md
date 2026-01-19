# Recetario Venezolano con Asistente IA

Este proyecto es una aplicación web que funciona como un recetario interactivo. Utiliza una base de datos local para almacenar platos tradicionales y se integra con la API de Google Gemini para ofrecer un asistente virtual capaz de responder dudas sobre cocina venezolana.

### Componentes del Sistema

* **Backend y Persistencia**: Se utiliza SQLite para la gestión de datos, permitiendo una consulta rápida de los ingredientes y pasos de preparación.
* **Inteligencia Artificial**: La aplicación conecta con el modelo Gemini 2.0 Flash para procesar consultas de los usuarios basándose en el contexto del recetario.
* **Interfaz de Usuario**: Desarrollada con Streamlit para ofrecer una navegación limpia y adaptable.
* **Seguridad**: Se implementó una arquitectura basada en variables de entorno para proteger las credenciales de la API, evitando la exposición de claves privadas en el repositorio.

### Requisitos Previos

Es necesario tener instalado Python 3.10 o superior y las librerías listadas en el archivo de requerimientos.

### Configuración e Instalación

1. **Clonación**: Descargue los archivos del repositorio en su máquina local.
2. **Dependencias**: Instale los paquetes necesarios ejecutando `pip install -r requirements.txt`.
3. **Credenciales**: Cree un archivo llamado `.env` en el directorio raíz y defina su llave de acceso de la siguiente manera: `GEMINI_API_KEY=su_clave_aqui`.
4. **Base de Datos**: Antes de iniciar la aplicación por primera vez, ejecute `python crear_base.py` para generar la estructura de tablas y los datos iniciales.
5. **Ejecución**: Inicie el servidor local con el comando `streamlit run recetario_web.py`.

### Estructura de Archivos

* `recetario_web.py`: Lógica principal de la aplicación e interfaz.
* `crear_base.py`: Script de inicialización de la base de datos SQLite.
* `.env`: Archivo de configuración privada (excluido de Git mediante .gitignore).
* `requirements.txt`: Lista de dependencias necesarias para el proyecto.