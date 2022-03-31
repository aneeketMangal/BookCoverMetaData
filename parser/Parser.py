# create a abstract parser class

from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def parseFile(self, filePath):
        pass

    @abstractmethod
    def parseDirectory(self, directoryPath):
        pass