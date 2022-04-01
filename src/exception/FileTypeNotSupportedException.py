class FileTypeNotSupportedException(Exception):
    def __init__(self, format):            
        message = "File format " + format + " is not supported"
        super().__init__(message)
        