import pytest
import os
from src.exception.NoSuchDirectoryException import NoSuchDirectoryException
from src.exception.NoSuchFileException import NoSuchFileException
from src.app import App
# def test_main():
   
#     result =  os.system("python main.py -d -p C:\\Users\\lenovo\\Desktop\\Adhoora\\academics\\year3\\cs305\\assignment3\\test\\resources -o C:\\Users\\lenovo\\Desktop\\Adhoora\\academics\\year3\\cs305\\assignment3\\test\\resources\\ou.xlsx")
    
#     assert True

def test_directory():
    directory = os.getcwd()
    path = os.path.join(directory, "test", "resources")
    out = os.path.join(directory, "test", "output.xlsx")
    type = "IMAGE"

    app = App(1, path, type, out)

    res = app.getMetaData()
    assert True


def test_file():
    directory = os.getcwd()
    path = os.path.join(directory, "test", "resources", "temp.jpeg")
    out = os.path.join(directory, "test", "output.xlsx")
    type = "IMAGE"

    app = App(0, path, type, out)

    res = app.getMetaData()
    assert True



def test_NoSuchDirectoryException():
    directory = os.getcwd()
    path = os.path.join(directory, "test", "someWrongDirectory")
    out = os.path.join(directory, "test", "output.xlsx")
    type = "IMAGE"

    with pytest.raises(NoSuchDirectoryException):
        app = App(1, path, type, out)
        res = app.getMetaData()

    assert True

def test_NoSuchFileException():
    directory = os.getcwd()
    path = os.path.join(directory, "test", "someWrongFile.jpg")
    out = os.path.join(directory, "test", "output.xlsx")
    type = "IMAGE"

    with pytest.raises(NoSuchFileException):
        app = App(0, path, type, out)
        res = app.getMetaData()

    assert True
