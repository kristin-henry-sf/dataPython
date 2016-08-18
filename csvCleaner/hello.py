import os

from cleanData import cleanFile
from convertFile import xlsToCsv

# based implementation in Flask app, will abstract this more later
UPLOAD_FOLDER = './tmp/'
CLEANED_FOLDER = './cleaned/'
RESULTS_FOLDER = './queryResults/'
ALLOWED_EXTENSIONS = set(['csv'])

# filename = './tmp/dummyData1.csv'
filename = './tmp/2010 Federal STEM Education Inventory Data Set.xls'


# Question: should I automatically rename file, replacing spaces with underscores?
csv_path = xlsToCsv(filename, UPLOAD_FOLDER)
print csv_path
# cleanFile(filename, CLEANED_FOLDER)