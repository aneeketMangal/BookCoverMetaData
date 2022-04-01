import os
from src.exception.NoSuchDirectoryException import NoSuchDirectoryException
from src.exception.NoSuchFileException import NoSuchFileException
from src.parse.ImageParser.ImageParser import ImageParser
from src.const.FileFormats import FileFormats
from src.exception.FileTypeNotSupportedException import FileTypeNotSupportedException
from src.out.ExcelOut import ExcelOut
import logging
class App():
    def __init__(self, directory, path, fileType, outFilePath):
        logging.info("Initializing App")
        logging.info(f"isDirectory: {directory}, path:{path}, fileType: {fileType}, outFilePath: {outFilePath}")
        self.__isFileType(fileType)
        self.__fileFormats = self.__getFileFormats(fileType)
        self.__parser = self.__getParser(fileType)
        self.__outFile = ExcelOut(outFilePath)
        if(directory):
            self.__isDirectory(path)
            self.__files = self.__getFilesInDirectory(path)
        else:
            self.__isFile(path)
            self.__files = [path]
        logging.info(f"Files recieved: {self.__files}")




    def getMetaData(self):
        logging.info("parseFiles called")
        output = self.__parser.parseFiles(self.__files)
        self.__outFile.write(output)
        return 1


    def __isDirectory(self, path):
        if(not os.path.isdir(path)):
            raise NoSuchDirectoryException(path)

    def __isFile(self, path):
        if(not os.path.isfile(path)):
            raise NoSuchFileException(path)

    def __isFileType(self, fileType):
        if(fileType not in FileFormats):
            raise FileTypeNotSupportedException(fileType)

    def __getFileFormats(self, fileType):
        return FileFormats[fileType]
       
    def __getParser(self, fileType):
        if(fileType == "IMAGE"):
            return ImageParser()
        else:
            return ImageParser()

    def __getFilesInDirectory(self, directoryPath):
        files = []
        for file in os.listdir(directoryPath):
            if file.endswith(tuple(self.__fileFormats)):
                files.append(os.path.join(directoryPath, file))

        return files

