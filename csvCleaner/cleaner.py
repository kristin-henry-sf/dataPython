import os, sys

from cleanData import cleanFile
from convertFile import checkFileType, readCSV

# based implementation in Flask app, will abstract this more later
UPLOAD_FOLDER = './tmp/'
CLEANED_FOLDER = './cleaned/'
RESULTS_FOLDER = './queryResults/'
ALLOWED_EXTENSIONS = set(['csv'])

filename = './tmp/dummyData1.csv'
# filename = './tmp/dummyData2.csv'
# filename = './tmp/dummyData3.csv'
# filename = './tmp/dummyData2.xlsx'
# filename = './tmp/STEMtest_1.csv'
#filename = './tmp/STEMtest_sparse_1.csv'
# filename = './tmp/STEMtest_sparse_2.csv'
# filename = './tmp/STEMtest_sparse_3.csv'
# filename = './tmp/STEMtest_full.csv'
# filename = './tmp/2010 Federal STEM Education Inventory Data Set.xls'
# filename = './tmp/Mobile_Food_Schedule.csv'
# Question: should I automatically rename file, replacing spaces with underscores?

# csv_path = checkFileType(filename, UPLOAD_FOLDER)
# print 'csv_path from main: ', csv_path

# readCSV(csv_path)

csv_path = filename


# Ok, this is a bit of a hack, but I'm doing it this way until I figure out a better way, needs to be cross-platform
# using '-' to find  next flags in command line args
cols = []
getCols = False

rows = []
getRows = False

i = 0
for arg in sys.argv:
	print 'arg: ', arg
	
	if arg == '-cols':
		cols.append(sys.argv[i+1])
	if arg == '-rows':
		rows.append(sys.argv[i+1])

	i+=1



	# # look for columns arg
	# if getCols:
	# 	if arg[0] != '-':
	# 		cols.append(arg)
	# 	else:
	# 		getCols = False
	# 		break
	# if arg =='-cols':
	# 	getCols = True

	# #  look for rows arg
	# if getRows:
	# 	if arg[0] != '-':
	# 		rows.append(arg)
	# 		print 'adding rows: ', rows
	# 	else:
	# 		getRows = False
	# 		break
	# if arg == '-rows':
	# 	print 'getting rows'
	# 	getRows = True


print '-----------------------'
print 'skin', '-skim' in sys.argv
print '-----------------------'

cleanFile(csv_path, CLEANED_FOLDER, skim='-skim' in sys.argv, columns = cols, rownums = rows, 
									json = '-json' in sys.argv, json2 = '-json2' in sys.argv)
 



# using to test merge


