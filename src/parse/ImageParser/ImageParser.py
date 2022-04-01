import logging
from src.parse.Parser import Parser
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter


class ImageParser(Parser):

    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tessaract\\tesseract.exe'

    """ 
        Main function to return all extracted metadata from a set of image files.
        @param files: List of image files to parse
        @return: List of lists of metadata extracted from the image files
    """

    def parseFiles(self, files):
        logging.debug(f"parseFiles called, files: {str(files)}")
        output = []
        for file in files:
            output.append(self.__parseFile(file))
        return output


    # Utility function to get the encoding of an image file
    def __getFileEncoding(self, filePath):
        try:
            text = pytesseract.image_to_string(
                Image.open(filePath),
            )

            data = pytesseract.image_to_data(
                Image.open(filePath),
            )
            blocks = pytesseract.image_to_boxes(
                Image.open(filePath),
            )
            logging.info(f"data: {str(data)}")
            logging.info(f"blocks: {blocks}")
            
            logging.info(f"File {filePath} has encoding: {text}")
            # xml = pytesseract.image_to_alto_xml(filePath)
            # print(xml)
            return text
        except Exception as e:
            logging.error(
                f"Error while parsing file: {filePath}, Error was {e}")
            return ""


    # Utility function to parse a single file and get the ISBN, Title, Author, Publisher
    def __parseFile(self, filePath):
        logging.debug(f"parseFile called, filePath: {filePath}")
        fileEncoding = self.__getFileEncoding(filePath)
        return [filePath, "ISBN", "Title", "Author", "Publisher", fileEncoding]


