# dataPython

The purpose of this project is to create a tool for cleaning up messy spreadsheets into well-formed csv files ready for analysis and saving to a database. Written in Python.

Currently, it's a command line tool.

## First, Quick and Dirty version
Python 2.7 (for now)
Note: this is very rough, first iteration

**run from command line with**

```python hello.py```

## Command line arguments

**Remove extra rows from top**

To remove extra rows above header rows, like the mailing address and logo of data source:

```python hello.py -skim```

* Must use '-skim' argv to indicate that the first row is not a header. 
	* Eventually, user intervention may not be needed and extra rows may be automatically detected as a pattern in the source file
* need more example files to test with, especially with extra top rows + nested headers with sparse content in first header row


**select specific columns**

```python hello.py -i 10-29, 45```

* index starts at 0 
* can select specific columns individually, and in ranges, by index
* new arguments after -i need to use a '-', to indicate that it's different flag

**select specific rows**

```python hello.py -rows 10``` or ```python hello.py -rows 1-20```
* These allow you to limit the number of rows. 
* If only one number, it's assumed you want first row and on.

```python hello.py -skim -rows 10 -i 1-4```
* This lets you remove extra headers and save specific rows and columns from the original file


**export in json format**

```python hello.py -json```
* saves data in json format
* still working on this...



## Dealing with Columns without headers

Some spreadsheets have data that is categorical, but in a wide format in the table, and without header names.

example data:

>hd1, hd2, hd3, __, __ , hd6, hd7

001, 001, 001, dt4, dt5, 001, 001

002, 002, 002, ___ , ___ , 002, 002

003, 003, 003, dt4, dt5, 003, 003

004, 004, 004, ___ , ___ , 004, 004

005, 005, 005, dt4, ___ , 005, 005





In many examples, the data in the column is repetative and can be extracted as the name for that column.

While the data in the column may be repetative, it might not be input in exactly the same way.  

For example, a column may have values of 'Middle (6-8)' and 'middle school (6-8)'. Or there may be many variations. For the sakeof simplicity, the shortest non-empty string becomes the header name. 


Also, when giving an extracted header name, I'm appending it with "****" so that it's easy to see which headers are extracted in the cleaned csv. Making it easier to go in and modify 'by hand' or with eventual UI for doing this task.





## Test files
Example csv files to test code with. Code expects them in the 'tmp' folder.
XLS files now converted to csv before starting cleaning process.

Cleaned/processed files are saved in 'cleaned' folder.

**dummyData1.csv**
* has extra cells at top of file, that are not headers and not data. need to be removed
* has extra numbers in cells below two collumns. need to be removed 

## Candidates for test files
**2010 Federal STEM Education Inventory Data Set on data.gov**
* has nested headers
* has commas in cells (text)
* an xls rather than csv file
* has column totals, for some columns
* http://catalog.data.gov/dataset/2010-federal-stem-education-inventory-data-set
* form used for data collection is also available

**Mobile Food Schedule**
* has dates, need converting, could be fun time series
* https://catalog.data.gov/dataset/mobile-food-schedule-7fd4d
* already in csv format



## Resources:
**python-excel.org**
* packages for working with Excel files: http://www.python-excel.org/
* pay attention to XML vulnerabilities and Excel files: http://xlrd.readthedocs.io/en/latest/vulnerabilities.html


