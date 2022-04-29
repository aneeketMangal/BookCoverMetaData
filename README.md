
> # CS305 Assignment 3
> Submitter name: Aneeket Mangal\
> Roll No.: 2019CSB1071\
> Course:  CS305 Software Engineering




## 1. What does this program do
This program is python based CLI (Command Line Interface) application which is used to extract metadata from image(s) containing pages of book.
Following information is extracted from images:
* Title
* Author
* Publisher
* ISBN


## 2. A description of how this program works
The program is used to extract metadata from image(s) containing pages of book.
-> The program collects all files which are to be processed. In case directory is provided, all files in the directory are collected and stored in array.
-> For each image, following process is followed.
-> First the raw text is extracted from the image using OCR. 
-> Then the text is cleaned and processed to extract metadata.
-> The program is optimized to account for casing error. For example "Pearson" is recognised as "pearSON" or "PeARsoN", the program will recognise both as "Pearson", thus improving accuracy of the program.

-> Extraction of Title:
  * The text chunk with largest height of enclosing box is considered as title. (an error 10% is considered as well). 
  * The title is mostly present in the largest font size on the page and hence this assumption is taken.

-> Extraction of ISBN:
  * ISBN is a 13/10 code assigned to each book. To extract the code, we count number of digits in the text and check if it is 13 or 10.
  * If so it is consodered to be ISBN.

-> Extraction of Author:
 * NER (Name Entity Recognition) has been used to extract author name.
 * ```en_core_web_trf``` model is employed to tokenize the text which is extracted from the image.
 * The program considers all the tokens which are recognized as ```PERSON``` as author. 
 * All supporting writers and editors are considered as authors as well.
 * All the authors are listed comma separated in the output.



-> Extraction of Publisher:
  * NER is used to extract publisher name.
  * The program considers all the tokens which are recognized as ```ORG``` as publisher.

-> Various corner cases have been covered to improve accuracy of the program.
-> For example: if some user provides a image with long text written on it(All the text is of same height), the program will consider the text as title. To avoid this, the program considers the text as title only if length of the text is less than 60 characters.
-> Finally all the extracted metadata is written to a xlsx file.
-> Following info is written into file
```
    [File name, Title, ISBN, Author, Publisher, File path]
```


## 3. How to compile and run this program
### Prerequisites:
* Python 3.8 or above
* pip version 20.0.2 or above
* This program was developed using Python 3.8.10 on Windows 11
* Install Tesseract software from the web and set the path to the executable file in the code.
* Install the other required python packages using the following command:
  ```
    pip install -r requirements.txt
  ```

* Logging is done to provide info of the program execution.
* Logs are by default present in the logs directory, in logs/logs.log file
### Instruction to run the program
* Locate to the root directory of the program.
* To use the program, run the following command
  ```
    python main.py -p <path_to_file/directory> 
  ```
* Use the following flags to provide location of image files and generated excel file
  -h, --help            show this help message and exit
  -path, -p             Path of directory/File containing book cover(s)
  -out -o               Path of output file
  -type, -t             File type of book cover(s) ()
  -directory, -d        Flag to specify wether the input path is a directory.
* Sample command to run the program is as below:
  ```
    python main.py -d -p test\resources -o test\output.xlsx
  ```
* In case you do not provide the output file, the program will generate a default output file in the results directory.


### Instruction to run the tests
* Locate to the root directory of the program.
* Run the following command to run the tests:
  ```
    python -m coverage run --source=src -m pytest --disable-warnings
  ```
* To generate the report:
  > **Generating HTML Report:**
  > ```
  > python -m coverage html
  > ```
  >
  > **Generating Terminal Report:**
  > ```
  > python -m coverage report
  > ```
  >
  > HTML report is present [here](htmlcov/index.html).



## 4. Provide a snapshot of a sample run
* The coverage of tests is 98% as tested using Coverage.py.

![img.png](docs/images/test.jpg)

![img.png](docs/images/coverage_report.jpg)




