import os

from cleanData import cleanFile

# based implementation in Flask app, will abstract this more later
UPLOAD_FOLDER = './tmp/'
CLEANED_FOLDER = './cleaned/'
RESULTS_FOLDER = './queryResults/'
ALLOWED_EXTENSIONS = set(['csv'])

filename = './tmp/dummyData1.csv'
cleanFile(filename, CLEANED_FOLDER)