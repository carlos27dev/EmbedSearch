# EmbeddingsProject

Este proyecto es una demostración de cómo extraer texto de archivos, generar embeddings usando Co:here, y realizar búsquedas semánticas usando un índice FAISS.

## Descripción

El proyecto permite a los usuarios cargar archivos (PDF, DOCX, TXT), extraer su contenido, generar embeddings para cada párrafo utilizando la API de Co:here y relizar consultas semánticas dentro del contenido utilizando FAISS.

## Instalación

1. Clonar el repositorio:
    ```sh
    git clone https://github.com/carlos27dev/EmbedSearch
    cd EmbeddingsProject
    ```

2. Crear y activar un entorno virtual:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instalar las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Configurar las variables de entorno:
    - Crear un archivo `.env` en la raíz del proyecto con tu API key de Co:here.
    ```env
    COHERE_API_KEY=tu_api_key
    ```

## Uso

1. Colocar los archivos que deseas procesar en el directorio `data/sample`.
2. Ejecutar el script principal:
    ```sh
    python main.py
    ```
3. El resultado de la búsqueda se mostrará en la consola.
4. El programa te pedirá que ingreses tu consulta:
   ```sh
    Please enter your query: (E.g.: How COVID affects this plan?):  
    ```
5. Los resultados se mostrarán en la consola.

## Autor

- **Carlos Arriaga** - [carlos27dev](https://github.com/carlos27dev)
