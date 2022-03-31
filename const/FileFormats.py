FileFormats = {
    "IMAGE": [".png", ".jpg", ".jpeg"],
    "AUDIO": [".mp3", ".wav", ".ogg"],
    "PDF": [".pdf"]
}


def getPath(fileType):
    return FileFormats[fileType]

