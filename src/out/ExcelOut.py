from src.out.Out import Out
from xlsxwriter import Workbook
import logging


class ExcelOut(Out):
    def __init__(self, filePath):
        super().__init__(filePath)
        logging.info("ExcelOut initialised")
        self.__path = filePath
        
        self.__workBook = Workbook(filePath)
        self.__sheet = self.__workBook.add_worksheet('Metadata')
        self.__writeRow(0, ['FileName', 'Title', 'ISBN', 'Author', 'Publisher', 'FilePath'])

    def __writeRow(self, row, rowContent):
        
        for column, cellContent in enumerate(rowContent):
            self.__sheet.write(row, column, cellContent)         
      
    def write(self, encodings):
        for encodingIndex, encoding in enumerate(encodings):
            self.__writeRow(encodingIndex+1, encoding)

        self.__workBook.close()