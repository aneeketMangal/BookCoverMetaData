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
            text = encoding.text.strip()
            possibleISBN = ""
            for char in text:
                if(char.isdigit()):
                    possibleISBN = possibleISBN + char
            
            if(len(possibleISBN) == 13 or len(possibleISBN) == 10):
                return possibleISBN
                           
        return NA

    """
        helper function to fetch title from the parsed results of OCR.
    """
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
        if(title == "" or len(title)> 60):
            return NA
        return title

    """
        helper function to fetch author from the parsed results of OCR.
    """
    @staticmethod
    def getAuthor(fileEncoding):
        logging.debug(f"filetokens: {[(i.text, i.label_) for i in fileEncoding.getTokens()]}")
        authors = set()
        for token in fileEncoding.getTokens():
            if token.label_ == "PERSON": # token with label_ == person are selected
                authors.add(token.text)
            
        if(len(authors) == 0): # if no authors are detected
            return NA
        return (", ").join(list(authors))

    """
        helper function to fetch publisher from the parsed results of OCR.
    """
    @staticmethod
    def getPublisher(fileEncoding):
        publishers =set()

        for token in fileEncoding.getTokens():
            if token.label_ == "ORG":
                publishers.add(token.text)

        if(len(publishers) == 0): # if no publishers are detected
            return NA
        return (", ").join(list(publishers))