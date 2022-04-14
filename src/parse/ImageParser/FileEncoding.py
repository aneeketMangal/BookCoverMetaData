class FileEncodingItem:
    def __init__(self, text, textHeight):
        self.text = text
        self.textHeight = int(textHeight)

class FileEncoding:
    def __init__(self):
        self.__encoding = []
        self.__text = ""
        self.tokens = []

    def addEncodingItem(self, text, height):
        self.__encoding.append(FileEncodingItem(text, height))

    def addText(self, text):
        self.__text = self.__text + text + " "

    def tokenize(self, tokenizer):
        self.tokens = tokenizer(self.__text)
        if(self.tokens.ents):
            # print(self.tokens.ents)
            for i in self.tokens.ents:
                print(i.text, i.label_)
            self.tokens = self.tokens.ents
        else:
            self.tokens = []

    def getEncoding(self):
        return self.__encoding

    def getText(self):
        return self.__text

    def getTokens(self):
        return self.tokens
