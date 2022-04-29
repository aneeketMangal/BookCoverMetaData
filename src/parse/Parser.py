# create a abstract parser class

from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def __init__(self):
        pass

    """
        The api endpoint for parsing all files in an array.
        @param files: List of files to parse
        @return: List of lists of metadata extracted from the image files
    """
    @abstractmethod
    def parseFiles(self, files):
        pass

    