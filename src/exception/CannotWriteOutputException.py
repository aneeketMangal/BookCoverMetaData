class CannotWriteOutputException(Exception):
    def __init__(self, message, filePath):
        finalMessage = f"Cannot write output to file: {filePath}, Error was {message}"
        super().__init__(message)
