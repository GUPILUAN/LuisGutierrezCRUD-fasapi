# FastAPI Libros API

Este es un ejemplo de una API RESTful para administrar una biblioteca de libros, desarrollada con FastAPI en Python.

## Características

- **CRUD completo:** Permite realizar operaciones básicas de creación, lectura, actualización y eliminación (CRUD) de libros.
- **Validación de datos:** Utiliza la validación de datos integrada de FastAPI para asegurar que los datos ingresados sean correctos.
- **Documentación automática:** FastAPI genera automáticamente una documentación interactiva basada en Swagger UI y ReDoc para explorar y probar la API.


## Requerimientos

- Python 3.12+
- Pip (administrador de paquetes de Python)

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/GUPILUAN/LuisGutierrezCRUD-fastapi.git
    ```

2. Ingresa al directorio del proyecto:

    ```bash
    cd LuisGutierrezCRUD-fastapi
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación:

    ```bash
    uvicorn main:app --reload
    ```
    O simplemente ▶️ el archivo `main.py` en tu IDE de preferencia.

2. Visita [http://localhost:8000/docs](http://localhost:8000/docs) en tu navegador para ver la documentación interactiva de la API.

