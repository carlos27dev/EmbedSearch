from abc import ABC, abstractmethod
from PyPDF2 import PdfReader
from docx import Document


class TextExtractor(ABC):
    """
    Clase base abstracta para la extracción de texto de archivos.
    """
    @abstractmethod
    def extract_text_impl(self, file_path):
        """
        Método abstracto para extraer texto de un archivo dado.

        :param file_path: Ruta del archivo desde el cual extraer el texto.
        :return: Una lista de párrafos extraídos del archivo.
        """
        pass

    def extract_text(self, file_path):
        """
        Método concreto, que se basa en la abstracción anterior, para extraer texto de un archivo dado,
        con manejo de errores.

        :param file_path: Ruta del archivo desde el cual extraer el texto.
        :return: Una lista de párrafos extraídos del archivo.
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
        Método estático para limpiar el texto, reemplazando caracteres de nueva línea y de tabulación, por espacios.

        :param text: El texto a limpiar.
        :return: Regresa texto limpio.
        """
        return text.replace('\n', ' ').replace('\t', ' ').strip()


class PDFTextExtractor(TextExtractor):
    """
    Clase para extraer texto de archivos PDF.
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
    Clase para extraer texto de archivos DOCX.
    """
    def extract_text_impl(self, file_path):
        document = Document(file_path)
        paragraphs = [paragraph.text for paragraph in document.paragraphs if paragraph.text.strip() != '']
        return paragraphs


class TXTTextExtractor(TextExtractor):
    """
    Clase para extraer texto de archivos TXT.
    """
    def extract_text_impl(self, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
            paragraphs = text.split('\n\n')
        return paragraphs
