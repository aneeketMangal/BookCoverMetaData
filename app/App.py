import os
from parser.ImageParser.ImageParser import ImageParser
from const.FileFormats import getPath
from exception.FileTypeNotSupportedException import FileTypeNotSupportedException


class App():
    def __init__(self, isDirectory, path, fileType):
        self.__fileFormats = getPath(fileType)
        self.__parser = self.__getParser(fileType)
        if(isDirectory):
            self.__files = self.__getFilesFromDirectory(path)
        else:
            self.__files = [path]



    def __getParser(fileType):
        if(fileType == "IMAGE"):
            return ImageParser()
        else:
            return FileTypeNotSupportedException(fileType)


    
    def __getFilesInDirectory(self, directoryPath):
        files = []
        for file in os.listdir(directoryPath):
            if file.endswith(self.__fileFormats):
                files.append(os.path.join(directoryPath, file))

        return files
        