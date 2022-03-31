from out.Out import Out
from xlwt import Workbook
import logging


class ExcelOut(Out):
    def __init__(self, filePath):
        super().__init__(filePath)
        logging.info("ExcelOut initialised")
        self.__path = filePath
        self.__workBook = Workbook()
        self.__sheet = self.__workBook.add_sheet('Metadata')
        self.__writeRow(0, ['FilePath', 'ISBN', 'Title', 'Author', 'Publisher'])

    def __writeRow(self, row, rowContent):
        for column, cellContent in enumerate(rowContent):
            self.__sheet.write(row, column, cellContent)         
    

    def write(self, encodings):
        for encodingIndex, encoding in enumerate(encodings):
            self.__writeRow(encodingIndex+1, encoding)

        self.__workBook.save(self.__path)