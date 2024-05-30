import os
from .extractor.text_extractor_factory import TextExtractorFactory


class FileProcessor:
    """
    Class to process files and extract text from them.
    """
    def __init__(self, path):
        """
        Constructor for the FileProcessor class, which takes the path to the directory containing the files.

        :param path: Path to the directory containing the files to be processed.
        """
        self.path = path

    def extract_text_from_files(self):
        """
        Extracts text from all files in the specified directory.

        :return: A list of texts extracted from the files.
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
