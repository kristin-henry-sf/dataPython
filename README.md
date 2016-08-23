# dataPython

The purpose of this project is to create a tool for cleaning up messy spreadsheets into well-formed csvfiles ready for analysis and saving to a database. Written in Python.

Currently, it's a commandline tool.

## First, Quick and Dirty version
Python 2.7 (for now)
Note: this is very rough, first iteration

**run from command line with**

```python hello.py```

**Commanline arguments**

if removing extra rows above header rows, use this:

```python hello.py top```

* **Must use 'top'** argv to indicate that the first row is not a header. Eventually, this may not be needed.

```python hello.py -i 10-29, 45```

* index starts at 0 
* can select specific columns individually, and in ranges, by index
* new arguments after -i need to use a '-', to indicate that it's different flag




## Test files
Example csv files to test code with. Code expects them in the 'tmp' folder.
XLS files now converted to csv before starting cleaning process.

Cleaned/processed files are saved in 'cleaned' folder.

**dummyData1.csv**
* has extra cells at top of file, that are not headers or data. need to be removed
* has extra numbers in cells below two collumns. need to be removed 

## Candidates for test files
**2010 Federal STEM Education Inventory Data Set on data.gov**
* has nested headers
* has commas in cells (text)
* an xls rather than csv file
* has column totals, for some columns
* http://catalog.data.gov/dataset/2010-federal-stem-education-inventory-data-set
* form used for data collection is also available



## Resources:
**python-excel.org**
* packages for working with Excel files: http://www.python-excel.org/
* pay attention to XML vulnerabilities and Excel files: http://xlrd.readthedocs.io/en/latest/vulnerabilities.html


