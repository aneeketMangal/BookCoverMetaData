from out.Out import Out
from xlwt import Workbook
  


class ExcelOut(Out):
    def __init__(self):
        self.__workBook = Workbook()
        self.__sheet = self.__workBook.add_sheet('Metadata')
        self.__writeRow(['FilePath', 'ISBN', 'Title', 'Author', 'Publisher'])

    def __writeRow(self, row, rowContent):
        for column, cellContent in enumerate(rowContent):
            self.__sheet.write(row, column, cellContent)         
    

    def writeEncodingsToFile(self, encodings, filePath):
        for encodingIndex, encoding in enumerate(encodings):
            self.__writeRow(encodingIndex, encoding)