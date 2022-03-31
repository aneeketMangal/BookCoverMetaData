import logging
from parse.Parser import Parser

class ImageParser(Parser):
    def __init__(self):
        pass

    def __getFileEncoding(self, filePath):
        pass

    def __parseFile(self, filePath):
        
        return [filePath, "ISBN", "Title", "Author", "Publisher"]

    def parseFiles(self, files):
        logging.debug(f"parseFiles called, files: {str(files)}")
        output = []
        for file in files:
            output.append(self.__parseFile(file))
        return output
