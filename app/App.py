import os
from parse.ImageParser.ImageParser import ImageParser
from const.FileFormats import getFileFormats
from exception.FileTypeNotSupportedException import FileTypeNotSupportedException
from out.ExcelOut import ExcelOut
import logging
class App():
    def __init__(self, isDirectory, path, fileType, outFilePath):
        logging.info("Initializing App")
        logging.info(f"isDirectory: {isDirectory}, path:{path}, fileType: {fileType}, outFilePath: {outFilePath}")
        self.__fileFormats = getFileFormats(fileType)
        self.__parser = self.__getParser(fileType)
        self.__outFile = ExcelOut(outFilePath)
        if(isDirectory):
            self.__files = self.__getFilesInDirectory(path)
        else:
            self.__files = [path]

        logging.info(f"files: {self.__files}")



    def __getParser(self, fileType):
        if(fileType == "IMAGE"):
            return ImageParser()
        else:
            raise FileTypeNotSupportedException(fileType)


    
    def __getFilesInDirectory(self, directoryPath):
        logging.info("main function called")
        files = []
        for file in os.listdir(directoryPath):
            if file.endswith(tuple(self.__fileFormats)):
                files.append(os.path.join(directoryPath, file))

        return files

    def parseFiles(self):
        logging.info("parseFiles called")
        output = self.__parser.parseFiles(self.__files)
        self.__outFile.write(output)


        