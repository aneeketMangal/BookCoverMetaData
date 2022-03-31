from abc import ABC, abstractmethod


class Out(ABC):
    @abstractmethod
    def __init__(self, filePath):
        pass


    
    '''
        The encoding should be of the following format
        [
            [filePath_1, isbn_1, title_1, author_1, publisher_1],
            ...
        ]
    '''

    @abstractmethod
    def write(self, encodings):
        pass
