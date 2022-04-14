
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


## 3. How to compile and run this program
### Prerequisites:
* Python 3.8 or above
* pip version 20.0.2 or above
* This program was developed using Python 3.8.10 on Windows 11
* Install Tesseract software from the web and set the path to the executable file in the code.
* Install the other required python packages using the following command:
  ```
    pip3 install -r requirements.txt
  ```

* Logging is done to provide info of the program execution.
* Logs are by default present in the logs directory, in logs/logs.log file
### Instruction to run the program
* Locate to the root directory of the program.
* To use the program, run the following command
  ```
    python3 main.py
  ```
* Use the following flags to provide location of image files and generated excel file
  -h, --help            show this help message and exit
  -path, -p             Path of directory/File containing book cover(s)
  -out -o               Path of output file
  -type, -t             File type of book cover(s)
  -directory, -d        Flag to specify wether the input path is a directory.
* Sample command to run the program is as below:
  ```
    python main.py -d -p C:\Users\lenovo\Desktop\Adhoora\academics\year3\cs305\assignment3\test\resources -o C:\Users\lenovo\Desktop\Adhoora\academics\year3\cs305\assignment3\test\output.xlsx
  ```


### Instruction to run the tests
* Locate to the root directory of the program.
* Run the following command to run the tests:
  ```
    python3 -m coverage run --source=src -m pytest 
  ```
* To generate the report:
  > **Generating HTML Report:**
  > ```
  > python3 -m coverage html
  > ```
  >
  > **Generating Terminal Report:**
  > ```
  > python3 -m coverage report
  > ```
  >
  > HTML report is present [here](htmlcov/index.html).



## 4. Provide a snapshot of a sample run
* The coverage of tests is 89% as tested using Coverage.py.

![img.png](docs/images/test.jpg)

![img.png](docs/images/coverage_report.jpg)

* Screenshot of test on LFW dataset
![img.png](docs/images/lfw_test.jpeg)



