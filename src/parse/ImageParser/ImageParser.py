import logging
import os
from src.parse.ImageParser.FetchMetadata import FetchMetadata
from src.parse.ImageParser.FileEncoding import FileEncoding
from src.parse.Parser import Parser
import spacy
import easyocr

NA = "Not found"

"""
    Concrete implementation of parser class for image files.
    This class is responsible for parsing the image files and extracting metadata.
"""
class ImageParser(Parser):

    def __init__(self):
        super().__init__()
        self.reader = easyocr.Reader(['en'])  # OCR utility
        self.tokenizer = spacy.load("en_core_web_trf") # NLP utility function to tokenize a string

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


    """
        This function helps to extract file encoding from the image file.
        The encoding is of type FileEncoding.
    """

    def __getFileEncoding(self, filePath):
        try:
            fileEncoding = FileEncoding()
            rawFileEncoding = self.reader.readtext(filePath)
            logging.debug(f"raw FIle encoding: {rawFileEncoding}")
            logging.debug(f"\nfile: {os.path.basename(filePath)}\nrawFileEncoding: {rawFileEncoding}")
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
        fileEncoding = self.__getFileEncoding(filePath)
        title = FetchMetadata.getTitle(fileEncoding)
        isbn = FetchMetadata.getISBN(fileEncoding)
        author = FetchMetadata.getAuthor(fileEncoding)
        publisher = FetchMetadata.getPublisher(fileEncoding)
        logging.debug(f"Title: {title}, ISBN: {isbn}, Author: {author}, Publisher: {publisher}")
        logging.debug(f"fileEncoding: {fileEncoding}")
        print("------------------File Processed-------------------")
        print(f"File: {os.path.basename(filePath)}\nTitle: {title}\nISBN: {isbn}\nAuthor: {author}\nPublisher: {publisher}")
        
        return [os.path.basename(filePath), title, isbn, author, publisher, filePath]
