# dataPython


## First, Quick and Dirty version
Python 2.7 (for now)
Note: this is very rough, first iteration

**run from command line with**

```python hello.py```


## Test files
Example csv files to test code with. In 'tmp' folder
Cleand files are saved in 'cleaned' folder

dummyData1.csv
* has extra cells at top of file, that are not headers or data. need to be removed
* has extra numbers in cells below two collumns. need to be removed 


## ToDo (yeah, this should probably be in git issues):
* remove extra numbers is cells below two collumns. This isn't working for dummyData1.csv
* make csv with summary table below main data rows, and make sure it's removed
* use xlrd to read excel files, and convert them to csv 
* longterm: make UI for guiding cleaning of particularly troublesome spreadsheets

## Resources:
**python-excel.org**
* packages for working with Excel files: http://www.python-excel.org/
* pay attention to XML vulnerabilities and Excel files: http://xlrd.readthedocs.io/en/latest/vulnerabilities.html

