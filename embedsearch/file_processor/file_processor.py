import os
from .extractor.text_extractor_factory import TextExtractorFactory


class FileProcessor:
    """
    Clase para procesar archivos y extraer texto de ellos.
    """
    def __init__(self, path):
        """
        Constructor de la clase FileProcessor, que recibe la ruta del directorio que contiene los archivos.

        :param path: Ruta del directorio que contiene los archivos a procesar.
        """
        self.path = path

    def extract_text_from_files(self):
        """
        Extrae texto de todos los archivos en el directorio especificado.

        :return: Una lista de los textos extraídos de los archivos.
        """
        texts = []
        for filename in os.listdir(self.path):
            file_path = os.path.join(self.path, filename)
            try:
                extractor = TextExtractorFactory.get_extractor(file_path)
                texts.append(extractor.extract_text(file_path))
            except ValueError as e:
                print(f"Error: {e} - {file_path}")
            except Exception as e:
                print(f"Unexpected error processing file '{file_path}': {e}")
        return texts
