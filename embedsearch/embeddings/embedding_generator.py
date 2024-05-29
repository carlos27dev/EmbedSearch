import cohere


class EmbeddingGenerator:
    """
    Clase para generar embeddings utilizando la API de Cohere.
    """
    def __init__(self, api_key):
        """
        Constructor de la clase EmbeddingGenerator, que recibe alguna clave de API de Cohere.

        :param api_key: Clave de API para autenticar las solicitudes a Cohere.
        """
        self.client = cohere.Client(api_key)

    def generate_embeddings(self, texts):
        """
        Método que genera embeddings para una lista de textos utilizando la API de Cohere.

        :param texts: Lista de textos para los cuales generar embeddings.
        :return: Lista de embeddings generados.
        :raises Exception: Si hay un error al llamar a la API de Cohere.
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
