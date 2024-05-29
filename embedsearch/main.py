import os
import pandas as pd
from dotenv import load_dotenv
from embedsearch.embeddings.embedding_generator import EmbeddingGenerator
from embedsearch.utils.utils import FileUtils

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
api_key = os.getenv('COHERE_API_KEY')


def main():
    """
    Punto de entrada principal para el programa.
    """
    # Consulta a realizar
    query = input("Please enter your query: (E.g.: How COVID affects this plan?): ")

    # Ruta del directorio que contiene los archivos a procesar
    files_path = 'data/sample'

    # Ruta donde se guardará el índice FAISS (Base de datos vectorial)
    faiss_index_path = 'results/faiss_index.bin'

    # Número de resultados a mostrar. (Es el número de vecinos más cercanos que se buscarán)
    k = 5

    # Verificar que el directorio de archivos existe
    FileUtils.check_files_path(files_path)

    # Procesar los archivos y extraer texto
    paragraphs = FileUtils.process_files(files_path)

    # Crear instancia del generador de embeddings con la API key
    generator = EmbeddingGenerator(api_key)

    # Generar y guardar los embeddings en un índice FAISS
    faiss_index = FileUtils.generate_and_save_embeddings(generator, paragraphs, faiss_index_path)

    print(f"\nFAISS index saved to {faiss_index_path}")

    # Realizar la búsqueda de la consulta en el índice FAISS
    results = FileUtils.search_query(query, generator, faiss_index, paragraphs, k)

    # Formatear los resultados de la búsqueda en un DataFrame de pandas
    results_df = pd.DataFrame(results, columns=['Paragraph', 'Distance'])

    # Mostrar los resultados de la búsqueda
    print("\nSearch results:")
    print(f"Query:'{query}'\nNearest neighbors:")
    print(results_df)


if __name__ == '__main__':
    main()
