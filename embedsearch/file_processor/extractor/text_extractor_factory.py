import os
from .text_extractor import PDFTextExtractor, DOCXTextExtractor, TXTTextExtractor


class TextExtractorFactory:
    """
    Fábrica para crear instancias de extractores de texto basados en la extensión del archivo.
    """
    _registry = {}

    @classmethod
    def register_extractor(cls, extension, extractor_cls):
        """
        Método que registra una clase de extractor para una extensión de archivo específica.

        :param extension: Extensión del archivo (p. ej.: '.pdf', '.docx').
        :param extractor_cls: Clase del extractor correspondiente.
        """
        cls._registry[extension] = extractor_cls

    @classmethod
    def get_extractor(cls, file_path):
        """
        Método que devuelve una instancia del extractor adecuado basado en la extensión del archivo.

        :param file_path: Ruta del archivo para el cual se requiere el extractor.
        :return: Instancia de la clase de extractor correspondiente.
        :raises ValueError: Si no hay extractor registrado para la extensión del archivo.
        """
        extension = os.path.splitext(file_path)[1]
        extractor_cls = cls._registry.get(extension)
        if extractor_cls is None:
            raise ValueError(f"No extractor available for file: {file_path}")
        return extractor_cls()


# Se registran los extractores para las extensiones que se requieren hasta ahora.
TextExtractorFactory.register_extractor('.pdf', PDFTextExtractor)
TextExtractorFactory.register_extractor('.docx', DOCXTextExtractor)
TextExtractorFactory.register_extractor('.txt', TXTTextExtractor)
