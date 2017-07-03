# dataPython

The purpose of this project is to create a tool for cleaning up messy spreadsheets into well-formed csv files ready for analysis and saving to a database. Written in Python.

Currently, it's a command line tool.

## First, Quick and Dirty version
Python 2.7 (for now)
Install Python with Anaconda (2.7 version): https://www.continuum.io/downloads

If you're running 3.x version of Python, install 2.7 in a venv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

Note: this is the first iteration. Though based on real-world examples, it still needs to be thoroughly tested.

**run from command line with**

```python cleaner.py```

# Command line arguments

## Remove extra rows from top

Sometimes, we get csv files with extra rows at the top of the file. These rows may be empty, or extra information like the mailing address and logo of data source.

To remove these, use 

```python cleaner.py -skim```

### Cases this works for:
* First rows are completely empty
* Extra top rows are less than 1/2 as many cells wide as the header/data rows

**Example that works:**

| conact@email.com   | ___ | ___  | ___ |
| **hd1.a** | hd1.b | hd1.c | hd2.a |
| ----- | ----- | ----- | ----- |
| 001   | 001   | 001   | 001   |
| 002   | 002   | 002   | 002   |


**Example that will fail:**

| contact@email.com   | ___ | 
| hd1 | hd2 | 
| ----- | ----- | 
| 001   | 001   | 
| 002   | 002   | 

The current implementation compares the length of the top rows to the 'normal' length of data rows, and this example has too few columns to use this feature.

### Notes: 
* If you know which row is the header, you may want to use the row selector flag instead
* need more example files to test with, especially with extra top rows + nested headers with sparse content in first header row


## select specific columns

```python cleaner.py -i 10-29, 45```

* index starts at 0 
* can select specific columns individually, and in ranges, by index
* new arguments after -i need to use a '-', to indicate that it's different flag

## select specific rows

```python cleaner.py -rows 10``` or ```python cleaner.py -rows 1-20```
* These allow you to limit the number of rows. 
* If only one number, it's assumed you want first row and on.

```python cleaner.py -skim -rows 10 -i 1-4```
* This lets you remove extra headers and save specific rows and columns from the original file


## export in json format

```python cleaner.py -json```
* saves data in json format
* still working on this...


## export in nested json format

```python cleaner.py -json2```
* two levels
* second header row is used as subheader
* ToDo: extract subheader from data when there is an empty subheader
* still working on this

| hd1   | _____ | _____ | hd2   |
| ----- | ----- | ----- | ----- |
| **hd1.a** | hd1.b | hd1.c | hd2.a |
| ----- | ----- | ----- | ----- |
| 001   | 001   | 001   | 001   |
| 002   | 002   | 002   | 002   |

would be rendered as 

```
{
	hd1: { hd1.a: 001, hd1.b: 001, hd1.c: 001},
 	hd2: { hd2.a: 001}
},
{
	hd1: { hd1.a: 002, hd1.b: 002, hd1.c: 002},
 	hd2: { hd2.a: 002}
}

```



## Dealing with Columns without headers

Some spreadsheets have data that is categorical, but in a wide format in the table, and without header names.

example data:

| hd1 | hd2 | hd3 | ____ | ____ | hd6 | hd7 |
| --- | --- | --- | ---- | ---- | --- | --- |
| 001 | 001 | 001 | dt4 | dt5 | 001 | 001 |
| 002 | 002 | 002 | ____ | ____ | 002 | 002 |
| 003 | 003 | 003 | dt4 | dt5 | 003 | 003 |
| 004 | 004 | 004 | ____ | ____ | 004 | 004 |
| 005 | 005 | 005 | dt4 | ____ | 005 | 005 |



In many examples, the data in the column is repetative and can be extracted as the name for that column.

While the data in the column may be repetative, it might not be input in exactly the same way. For example, a column may have values of 'Middle (6-8)' and 'middle school (6-8)'. Or there may be many variations. For the sake of simplicity, the shortest non-empty string becomes the header name. 


When giving a column an extracted header name, currently prepending it with "****" 
* so that it's easy to see which headers are extracted in the cleaned csv. Making it easier to go in and modify 'by hand' or with eventual UI for doing this task.

Headerless columns, with only numerical data, are named 'num' + the index of the column. 


# Coding conventions and reasoning
* names: Currently, variable names are in underscore_style and functions are in camelCaseStyle
* Python version: 2.7 (soon will be Python3 compliant)

## why lists of lists?
In the code, the data from the csv is in list of lists, instead of in a dataframe. Why? 
* The raw data may not have a header, so there are no labels at all for a dataframe
* The raw data may not be consistently sized, and may contain multiple 'tables' and different dimensions
* The raw data may have missing column names, in addition to multiple and heirarchical header rows


# Testing
## Unit Testing

Unit tests are currently in development.

To run existing tests:

```
python test_CleanData.py
```


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


