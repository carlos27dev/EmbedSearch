import os
import numpy as np
from embedsearch.file_processor.file_processor import FileProcessor
from embedsearch.faiss_index.faiss_index import FaissIndex


class FileUtils:
    @staticmethod
    def check_files_path(files_path):
        """
        Método que verifica que el directorio de archivos exista.

        :param files_path: La ruta del directorio que contiene los archivos.
        :raises FileNotFoundError: Si el directorio no existe.
        """
        if not os.path.exists(files_path):
            raise FileNotFoundError(f"No such file or directory: '{files_path}'")

    @staticmethod
    def process_files(files_path):
        """
        Método que procesa los archivos y extrae el texto de ellos.

        :param files_path: La ruta del directorio que contiene los archivos.
        :return: Una lista de párrafos extraídos de los archivos.
        """
        processor = FileProcessor(files_path)
        texts = processor.extract_text_from_files()
        paragraphs = [paragraph for text in texts for paragraph in text]
        return paragraphs

    @staticmethod
    def generate_and_save_embeddings(generator, paragraphs, faiss_index_path):
        """
        Método que genera embeddings para los párrafos, crea un índice FAISS y lo guarda.

        :param generator: Instancia del generador de embeddings.
        :param paragraphs: Lista de párrafos para generar embeddings.
        :param faiss_index_path: La ruta donde se guardará el índice FAISS.
        :return: El índice FAISS creado con los embeddings generados.
        """
        embeddings = [generator.generate_embeddings([paragraph]) for paragraph in paragraphs]

        embeddings = np.array(embeddings).squeeze()
        dimension = len(embeddings[0])

        faiss_index = FaissIndex(dimension)
        faiss_index.add_embeddings(embeddings)
        faiss_index.save_index(faiss_index_path)

        return faiss_index

    @staticmethod
    def search_query(query, generator, faiss_index, paragraphs, k):
        """
        Método que genera embeddings para la consulta y realiza la búsqueda en el índice FAISS.

        :param query: La consulta para la cual se generarán embeddings.
        :param generator: Instancia del generador de embeddings.
        :param faiss_index: El índice FAISS donde se realizará la búsqueda.
        :param paragraphs: Lista de párrafos de los cuales se generaron los embeddings.
        :param k: El número de vecinos más cercanos a buscar.
        :return: Una lista de tuplas con los párrafos más cercanos y sus distancias respectivas.
        """
        query_embeddings = generator.generate_embeddings([query])
        distances, indices = faiss_index.search(query_embeddings, k)

        results = [(paragraphs[index], distances[0][i]) for i, index in enumerate(indices[0])]
        return results
