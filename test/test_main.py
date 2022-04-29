import pytest
import os
from src.exception.FileTypeNotSupportedException import FileTypeNotSupportedException
from src.exception.NoSuchDirectoryException import NoSuchDirectoryException
from src.exception.NoSuchFileException import NoSuchFileException
from src.app import App
import warnings

@pytest.fixture(scope="session", autouse=True)
def before(request):
    warnings.filterwarnings("ignore")


def test_directory():
    directory = os.getcwd()
    path = os.path.join(directory, "test", "resources")
    out = os.path.join(directory, "test", "results","output_directory.xlsx")
    type = "IMAGE"

    app = App(1, path, type, out)

    res = app.getMetaData()
    assert True


def test_file():
    directory = os.getcwd()
    path = os.path.join(directory, "test", "resources", "test_4.png")
    out = os.path.join(directory, "test", "results","output_file.xlsx")
    type = "IMAGE"

    app = App(0, path, type, out)

    res = app.getMetaData()
    assert True



def test_NoSuchDirectoryException():
    directory = os.getcwd()
    path = os.path.join(directory, "test", "someWrongDirectory")
    out = os.path.join(directory, "test", "results","output_NoSuchDirectory.xlsx")

    type = "IMAGE"

    with pytest.raises(NoSuchDirectoryException):
        app = App(1, path, type, out)
        res = app.getMetaData()

    assert True

def test_NoSuchFileException():
    directory = os.getcwd()
    path = os.path.join(directory, "test", "someWrongFile.jpg")
    out = os.path.join(directory, "test", "results","output_NoSuchFile.xlsx")

    type = "IMAGE"

    with pytest.raises(NoSuchFileException):
        app = App(0, path, type, out)
        res = app.getMetaData()

    assert True

def test_FileTypeNotSupportedException():
    directory = os.getcwd()
    path = os.path.join(directory, "test", "resources", "test_6.pdf")
    out = os.path.join(directory, "test", "results","output_FileTypeNotSupported.xlsx")
    type = "PDF"

    with pytest.raises(FileTypeNotSupportedException):
        app = App(0, path, type, out)
        res = app.getMetaData()

    assert True

def test_titleTooLong():
    directory = os.getcwd()
    path = os.path.join(directory, "test", "resources", "test_12.jpeg")
    out = os.path.join(directory, "test", "results","output_titleTooLong.xlsx")
    type = "IMAGE"

    app = App(0, path, type, out)

    res = app.getMetaData()
    assert True

def test_emptyPage():
    directory = os.getcwd()
    path = os.path.join(directory, "test", "resources", "test_11.jpg")
    out = os.path.join(directory, "test", "results","output_emptyPage.xlsx")
    type = "IMAGE"

    app = App(0, path, type, out)

    res = app.getMetaData()
    assert True
