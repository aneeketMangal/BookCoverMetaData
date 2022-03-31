
import argparse
import re
ArgParser = None

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

if __name__  == "__main__":
    initializeArgParser()
    args = ArgParser.parse_args()

    print(args)

