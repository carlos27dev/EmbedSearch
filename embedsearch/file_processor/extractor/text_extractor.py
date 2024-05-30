from abc import ABC, abstractmethod
from PyPDF2 import PdfReader
from docx import Document


class TextExtractor(ABC):
    """
    Abstract base class for extracting text from files.
    """
    @abstractmethod
    def extract_text_impl(self, file_path):
        """
        Abstract method to extract text from a given file.

        :param file_path: Path to the file from which to extract text.
        :return: A list of paragraphs extracted from the file.
        """
        pass

    def extract_text(self, file_path):
        """
        Concrete method, based on the above abstraction, to extract text from a given file with error handling.

        :param file_path: Path to the file from which to extract text.
        :return: A list of paragraphs extracted from the file.
        """
        paragraphs = []
        try:
            paragraphs = self.extract_text_impl(file_path)
        except FileNotFoundError:
            print(f"Error: File not found in '{file_path}'.")
        except Exception as e:
            print(f"Error while reading file: '{file_path}': {e}")
        return [self.clean_text(paragraph) for paragraph in paragraphs]

    @staticmethod
    def clean_text(text):
        """
        Static method to clean text by replacing both newline and tab characters with spaces.

        :param text: The text to clean.
        :return: Cleaned text.
        """
        return text.replace('\n', ' ').replace('\t', ' ').strip()


class PDFTextExtractor(TextExtractor):
    """
    Class to extract text from PDF files.
    """
    def extract_text_impl(self, file_path):
        paragraphs = []
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            for page_num in range(len(reader.pages)):
                text = reader.pages[page_num].extract_text()
                if text:
                    paragraphs.extend(text.split('\n\n'))
        return paragraphs


class DOCXTextExtractor(TextExtractor):
    """
    Class to extract text from DOCX files.
    """
    def extract_text_impl(self, file_path):
        document = Document(file_path)
        paragraphs = [paragraph.text for paragraph in document.paragraphs if paragraph.text.strip() != '']
        return paragraphs


class TXTTextExtractor(TextExtractor):
    """
    Class to extract text from TXT files.
    """
    def extract_text_impl(self, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
            paragraphs = text.split('\n\n')
        return paragraphs
