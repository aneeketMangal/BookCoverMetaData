
class NoSuchFileException(Exception):
    def __init__(self, filePath):
        self.filePath = filePath
        self.message = f"No such directory: {self.filePath}"
        super().__init__(self.message)