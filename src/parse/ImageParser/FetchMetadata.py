NA = "Not found"
import logging
class FetchMetadata:
    
    """
        helper function to fetch ISBN number from the parsed results of OCR
        Currently it only checks of 13 digit ISBN number which are standard after 2007.
        It only detects ISBN number only if its present as a single string on the book page covers.
    """
    @staticmethod
    def getISBN(fileEncoding):
        for encoding in fileEncoding.getEncoding():
            if len(encoding.text) == 13 and encoding.text.isnumeric():
                return encoding.text
        return NA

    @staticmethod
    def getTitle(fileEncoding):
        title = ""
        maxVal = max([encoding.textHeight for encoding in fileEncoding.getEncoding()], default=1e9)
        logging.debug(f"maxVal: {maxVal}")
        logging.debug(f"fileEncoding.getEncoding(): {[(i.text, i.textHeight) for i in fileEncoding.getEncoding()]}")
        for encoding in fileEncoding.getEncoding():
            if encoding.textHeight >= 0.9* maxVal:
                title = title + " " + encoding.text
        title = title.strip()
        if(title == ""):
            return NA
        return title

    @staticmethod
    def getAuthor(fileEncoding):
        logging.debug(f"filetokens: {[(i.text, i.label_) for i in fileEncoding.getTokens()]}")
        authors = set()
        for token in fileEncoding.getTokens():
            if token.label_ == "PERSON":
                authors.add(token.text)
            
        if(len(authors) == 0):
            return NA
        return (", ").join(list(authors))
        # return NA

    @staticmethod
    def getPublisher(fileEncoding):
        for token in fileEncoding.getTokens():
            if token.label_ == "ORG":
                return token.text
        return NA