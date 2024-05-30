import cohere


class EmbeddingGenerator:
    """
    Class to generate embeddings using the Co:here API.
    """
    def __init__(self, api_key):
        """
        Constructor for the EmbeddingGenerator class, which takes a Co:here API key .

        :param api_key: API key to authenticate requests to Co:here.
        """
        self.client = cohere.Client(api_key)

    def generate_embeddings(self, texts):
        """
        Method to generate embeddings for a list of texts using the Co:here API.

        :param texts: List of texts for which to generate embeddings.
        :return: List of generated embeddings.
        :raises Exception: If there is an error calling the Co:here API.
        """
        try:
            response = self.client.embed(
                texts=texts,
                model="embed-english-v3.0",
                input_type="search_query"
            )
            return response.embeddings
        except cohere.InternalServerError as e:
            print(f"Cohere Internal Server Error: {e}")
            raise
        except Exception as e:
            print(f"Unexpected Error: {e}")
            raise
