import faiss
import numpy as np


class FaissIndex:
    """
    Clase para gestionar un índice FAISS.
    """
    def __init__(self, dimension):
        """
        Constructor de FaissIndex, que recibe la dimensión de los embeddings.

        :param dimension: Dimensión de los embeddings.
        """
        self.dimension = dimension

        # El tipo IndexFlatL2 realiza búsquedas basadas en la métrica de distancia L2 (euclidiana).
        self.index = faiss.IndexFlatL2(dimension)

    def save_index(self, file_path):
        """
        Guarda el índice en un archivo.

        :param file_path: Ruta del archivo donde guardar el índice.
        """
        try:
            faiss.write_index(self.index, file_path)
        except Exception as e:
            print(f"Error saving FAISS index: {e}")
            raise

    def add_embeddings(self, embeddings):
        """
        Añade embeddings al índice.

        :param embeddings: Lista de embeddings a añadir al índice.
        """
        try:
            embeddings = np.array(embeddings).astype('float32')
            self.index.add(embeddings)
        except Exception as e:
            print(f"Error adding embeddings: {e}")
            raise

    def search(self, query_embeddings, k=5):
        """
        Realiza una búsqueda en el índice.

        :param query_embeddings: Embeddings de consulta.
        :param k: Número de vecinos más cercanos a devolver.
        :return: Distancias e índices de los vecinos más cercanos.
        """
        try:
            query_embeddings = np.array(query_embeddings).astype('float32')
            distances, indices = self.index.search(query_embeddings, k)
            return distances, indices
        except Exception as e:
            print(f"Error searching index: {e}")
            raise
