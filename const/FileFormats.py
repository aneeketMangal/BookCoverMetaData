from exception.FileTypeNotSupportedException import FileTypeNotSupportedException
FileFormats = {
    "IMAGE": [".png", ".jpg", ".jpeg"],
    "AUDIO": [".mp3", ".wav", ".ogg"],
    "PDF": [".pdf"]
}


def getFileFormats(fileType):
    if(fileType in FileFormats):
        return FileFormats[fileType]
    else:
        raise FileTypeNotSupportedException(fileType)

