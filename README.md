# dataPython

The purpose of this project is to create a tool for cleaning up messy spreadsheets into well-formed csvfiles ready for analysis and saving to a database. Written in Python.

Currently, it's a commandline tool.

## First, Quick and Dirty version
Python 2.7 (for now)
Note: this is very rough, first iteration

**run from command line with**

```python hello.py```


## Test files
Example csv files to test code with. Code expects them in the 'tmp' folder.

Cleaned/processed files are saved in 'cleaned' folder.

dummyData1.csv
* has extra cells at top of file, that are not headers or data. need to be removed
* has extra numbers in cells below two collumns. need to be removed 


## Resources:
**python-excel.org**
* packages for working with Excel files: http://www.python-excel.org/
* pay attention to XML vulnerabilities and Excel files: http://xlrd.readthedocs.io/en/latest/vulnerabilities.html

