import logging
import os
from src.parse.ImageParser.FetchMetadata import FetchMetadata
from src.parse.ImageParser.FileEncoding import FileEncoding
from src.parse.Parser import Parser
import pytesseract
from PIL import Image
import spacy

import easyocr

NA = "Not found"


class ImageParser(Parser):

    def __init__(self):
        super().__init__()
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tessaract\\tesseract.exe'
        self.tokenizer = spacy.load("en_core_web_sm", disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])
        self.reader = easyocr.Reader(['en'])

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


    def __getImageObject(self, filePath:str):
        try:
            img = Image.open(filePath)
            return img
        except Exception as e:
            logging.error(
                f"Error while parsing file: {filePath}, Error was {e}")
            return None

    def __getFileEncoding(self, filePath: str):
        try:
            fileEncoding = FileEncoding()
            rawFileEncoding = pytesseract.image_to_data(self.__getImageObject(filePath), output_type=pytesseract.Output.DICT)
            
            logging.debug(f"\nfile: {os.path.basename(filePath)}\nrawFileEncoding: {rawFileEncoding['text']}\nheight: {rawFileEncoding['height']}\n")
            for i in range(len(rawFileEncoding['text'])):
                if(rawFileEncoding['text'][i].strip() != ""):
                    fileEncoding.addEncodingItem(rawFileEncoding['text'][i].strip(), rawFileEncoding['height'][i])
                    fileEncoding.addText(rawFileEncoding['text'][i].strip())
            # return fileEncoding
            fileEncoding.tokenize(self.tokenizer)
            return fileEncoding
        except Exception as e:
            return FileEncoding()

    def __getFileEncodingTe(self, filePath):
        try:
            fileEncoding = FileEncoding()
            rawFileEncoding = self.reader.readtext(filePath)
            logging.debug(f"\nfile: {os.path.basename(filePath)}\nrawFileEncoding: {rawFileEncoding['text']}\nheight: {rawFileEncoding['height']}\n")
            for i in range(len(rawFileEncoding['text'])):
                if(rawFileEncoding['text'][i].strip() != ""):
                    fileEncoding.addEncodingItem(rawFileEncoding['text'][i].strip(), rawFileEncoding['height'][i])
                    fileEncoding.addText(rawFileEncoding['text'][i].strip())
            # return fileEncoding
            for encoding in rawFileEncoding:
                boxDimenssions = encoding[0]
                text = encoding[1]
                textHeight =  boxDimenssions[2][1] - boxDimenssions[1][1]
                fileEncoding.addEncodingItem(text, textHeight)
                fileEncoding.addText(text)
            fileEncoding.tokenize(self.tokenizer)
            return fileEncoding

        except Exception as e:
            return FileEncoding()


    # Utility function to parse a single file and get the ISBN, Title, Author, Publisher
    def __parseFile(self, filePath):
        logging.debug(f"parseFile called, filePath: {filePath}")
        fileEncoding = self.__getFileEncodingTe(filePath)
        title = FetchMetadata.getTitle(fileEncoding)
        isbn = FetchMetadata.getISBN(fileEncoding)
        author = FetchMetadata.getAuthor(fileEncoding)
        publisher = FetchMetadata.getPublisher(fileEncoding)
        logging.debug(f"fileEncoding: {fileEncoding}")
        return [filePath, isbn, title, author, publisher]
