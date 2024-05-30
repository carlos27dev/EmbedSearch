import os
from .text_extractor import PDFTextExtractor, DOCXTextExtractor, TXTTextExtractor


class TextExtractorFactory:
    """
    Factory to create instances of text extractors based on the file extension.
    """
    _registry = {}

    @classmethod
    def register_extractor(cls, extension, extractor_cls):
        """
        Method to register an extractor class for a specific file extension.

        :param extension: File extension (e.g., '.pdf', '.docx').
        :param extractor_cls: Corresponding extractor class.
        """
        cls._registry[extension] = extractor_cls

    @classmethod
    def get_extractor(cls, file_path):
        """
        Method to return an instance of the appropriate extractor based on the file extension.

        :param file_path: Path to the file for which the extractor is required.
        :return: Instance of the corresponding extractor class.
        :raises ValueError: If no extractor is registered for the file extension.
        """
        extension = os.path.splitext(file_path)[1]
        extractor_cls = cls._registry.get(extension)
        if extractor_cls is None:
            raise ValueError(f"No extractor available for file: {file_path}")
        return extractor_cls()


# Register extractors for the required file extensions.
TextExtractorFactory.register_extractor('.pdf', PDFTextExtractor)
TextExtractorFactory.register_extractor('.docx', DOCXTextExtractor)
TextExtractorFactory.register_extractor('.txt', TXTTextExtractor)
