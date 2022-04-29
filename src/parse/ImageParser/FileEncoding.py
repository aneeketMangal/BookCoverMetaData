
class FileEncodingItem:
    """
        This class is a storage class, for holding text chunks extracted from the OCR.
        It stores text and its height.
    """
    def __init__(self, text, textHeight):
        self.text = text
        self.textHeight = int(textHeight)


class Token:
    """
        This class stores a token extracted from NER(Named Entity Recognition).
        It stores the text and its label (type of entity)
    """
    def __init__(self, text, label):
        self.text = text
        self.label_ = label


class FileEncoding:
    """
        Utility class to handle encoding extracted from the file.
        Performs the task of assorting the extracted data and storing in a required format.

    """

    def __init__(self):
        self.__encoding = []
        self.__text = ""
        self.__tokens = []

    # add an encoding item (text chunk)
    def addEncodingItem(self, text, height):
        self.__encoding.append(FileEncodingItem(text, height))

    # add text to the encoding
    def addText(self, text):
        self.__text = self.__text + " " + text

    """
        This function manipulates the OCR results and returns a list of tokens.
        The tokens are of type Token.
    """
    def tokenize(self, tokenizer):
        tokensNormal = tokenizer(self.__text) # tokenize the raw text
        tokensNames = tokenizer(self.__text.title()) # tokenize the raw text with title case (for NER)
        tempArray = []
        # first extract the tokens from the title cased text (Names are recognised better in title case)
        # then add the tokens from the normal text
        if (tokensNames.ents):
            for ent in tokensNames.ents:
                tempToken = Token(ent.text, ent.label_)
                tempToken.text = tempToken.text.replace(", ", " ")
                if (tempToken.label_ == "PERSON" or tempToken.label_ == "ORG"):
                    self.__tokens.append(tempToken)
                    tempArray += [tempToken.text.lower()]
                    tempArray += [ent.text.lower()]
                    tempArray += [i.lower() for i in ent.text.split(", ")]
        if (tokensNormal.ents):
            for ent in tokensNormal.ents:
                tempToken = Token(ent.text, ent.label_)
                tempToken.text = tempToken.text.replace(", ", " ")
                # keeping track that there is no duplication of text
                if ((tempToken.label_ == "PERSON" or tempToken.label_ == "ORG")
                        and (tempToken.text.lower() not in tempArray)):
                    self.__tokens.append(tempToken)
                    tempArray += [tempToken.text.lower()]
                    tempArray += [ent.text.lower()]
                    tempArray += [i.lower() for i in ent.text.split(", ")]
        else:
            self.__tokens = []

    def getEncoding(self):
        return self.__encoding

    def getTokens(self):
        return self.__tokens
