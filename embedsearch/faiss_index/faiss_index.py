import faiss
import numpy as np


class FaissIndex:
    """
    Class to manage a FAISS index.
    """
    def __init__(self, dimension):
        """
        Constructor for FaissIndex class, which takes the dimension of the embeddings.

        :param dimension: Dimension of the embeddings.
        """
        self.dimension = dimension

        # The IndexFlatL2 type performs searches based on the L2 (Euclidean) distance metric.
        self.index = faiss.IndexFlatL2(dimension)

    def save_index(self, file_path):
        """
        Saves the index to a file.

        :param file_path: Path to the file where the index will be saved.
        """
        try:
            faiss.write_index(self.index, file_path)
        except Exception as e:
            print(f"Error saving FAISS index: {e}")
            raise

    def add_embeddings(self, embeddings):
        """
        Adds embeddings to the index.

        :param embeddings: List of embeddings to add to the index.
        """
        try:
            embeddings = np.array(embeddings).astype('float32')
            self.index.add(embeddings)
        except Exception as e:
            print(f"Error adding embeddings: {e}")
            raise

    def search(self, query_embeddings, k=5):
        """
        Performs a search on the index.

        :param query_embeddings: Query embeddings.
        :param k: Number of nearest neighbors to return.
        :return: Distances and indices of the nearest neighbors.
        """
        try:
            query_embeddings = np.array(query_embeddings).astype('float32')
            distances, indices = self.index.search(query_embeddings, k)
            return distances, indices
        except Exception as e:
            print(f"Error searching index: {e}")
            raise
