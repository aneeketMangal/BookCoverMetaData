
import argparse
from app.App import App
ArgParser = None
import logging

logging.basicConfig(
    filename= "logs/log.txt",
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

def initializeArgParser():
    global ArgParser
    ArgParser = argparse.ArgumentParser(description='Extracts metadata from book covers.')

    ArgParser.add_argument(
        "-path", "-p",
        required=True,
        nargs = 1, 
        type = str,
        help = "Path of directory/File containing book cover(s)"
    )

    ArgParser.add_argument(
        "-out", "-o",
        required=True,
        nargs = "*",
        type = str,
        help = "Path of output file"
    )

    ArgParser.add_argument(
        "-type", "-t",
        default="IMAGE",
        nargs = 1,
        type = str,
        help = "File type of book cover(s)"
    )     

    ArgParser.add_argument(
        "-directory", "-d",
        action="store_true",
        help = "Flag to specify wether the input path is a directory."
    )

    logging.info("Argument parser initialized.")



if __name__  == "__main__":
    initializeArgParser()
    args = ArgParser.parse_args()
    App = App(args.directory, args.path[0], args.type, args.out[0])
    App.parseFiles()

