
class NoSuchDirectoryException(Exception):
    def __init__(self, directoryPath):
        self.directoryPath = directoryPath
        self.message = f"No such directory: {self.directoryPath}"
        super().__init__(self.message)