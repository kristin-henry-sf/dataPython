import os
import csv
import numbers
# import pandas as pd
from collections import Counter

# adding a line here, to practice some git skills


# This is for dealing with csv's that have forced empty cells in extra rows (non data, non header)
def nibble(row):
	nibbled_row = []
	save = False

	# first check if we want to nibble/trim this row
	# we don't want to nibble the header rows
	empties = 0
	for elem in reversed(row):
		if(getType(elem) == 'empty'):
			empties += 1
		else:
			break

	# ToDo: come up with better test, this only works if rows are long. Won't work for rows with 2 or so elements.
	#  If less than half of cells at end of row are empty, we may have data or header
	if(empties < len(row)/2):
		return row

	# go ahead and nibble this row. It's not full data or heaader rows
	for elem in reversed(row):
		if(save == False):
			if getType(elem) == 'empty':
				continue
			else:
				save = True
				nibbled_row.append(elem)
		else:
			nibbled_row.append(elem)

	return nibbled_row[::-1]


# super simple type checking, anything other than int or float will be str or empty
def getType(elem):
	try:
		float(elem)
		return 'num'
	except ValueError:
		if elem == '':
			return 'empty'
	return 'str'


def getTypesPattern(row):
	rowTypes = []
	for elem in row:
		rowTypes.append(getType(elem))
	return rowTypes


def isRowEmpty(pattern):
	for elem in pattern:
		if elem != 'empty':
			return False
	return True


def getRows(file_path):
	rows = []

	# print open(file_path).read().index('\0')
	with open(file_path, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			# print row
			rows.append(row)
		f.close()
	return rows
	

def cleanUnnamed(rows):
	row = rows[0] 	# get the first row, only one that could have 'Unnamed: # ' cells
	rows = rows[1:] # save the rest of the rows
	
	newrow = []
	for cell in row:
		if 'Unnamed' in cell:
			newrow.append('')
		else:
			newrow.append(cell)
	rows.insert(0, newrow) # put our cleaned row back as first row 
	
	return rows


def getRowTypePatterns(rows):
	row_type_patterns = []
	for row in rows:
		pattern = getTypesPattern(row)
		row_type_patterns.append(tuple(pattern))
	return Counter(row_type_patterns).most_common()


def getCommonRowLengths(rows):
	lengths = []
	for row in rows:
		lengths.append(len(row))

	return Counter(lengths)


# ToDo: clean this up, so it returns fewer things!!!! 
def removeEmptyRows(old_rows):
	rows = []
	for row in old_rows: 
		pattern = getTypesPattern(row)
		if isRowEmpty(pattern) == False:
			rows.append(row)
	return rows


# ToDo: make sure we don't remove heaaders that are empty in last cells
def removeExtraTopRows(rows, common_row_length):
	i = 0
	for row in rows:
		i+=1
		row = nibble(row)
		if len(row) == common_row_length:
			break
	return rows[i-1:]


def removeSummaryTable(rows, common_row_length):
	i = len(rows)
	for row in reversed(rows):
		i-=1
		row = nibble(row)
		print 'nibbled: ', row
		if len(row) >= common_row_length/2:
			break
	return rows[:i+1]


def flattenHeaders(keepRows):
	# This is not as robust as it can be, keeping it simple for now
	# Assumption: first rows are likely to be headers, and when pattern becomes 'common', it's data
	# Assumption: headers will not have numbers as names --> header rows don't have number types in them
	headers = []
	for row in keepRows:
		print row
		if 'num' not in getTypesPattern(row):
			headers.append(row)
		else:
			break

	print '------'

	if len(headers) > 1:

		# remove the old headers 
		keepRows = keepRows[len(headers):]

		new_header = []

		i = 0
		pre = ''
		post = ''
		for item in headers[0]:

			types = (getType(headers[0][i]), getType(headers[1][i]))

			if types == ('str', 'str'):
				pre = headers[0][i]
				post = " " + headers[1][i]
			if types == ('empty', 'str'):
				post = " " + headers[1][i]
			if types == ('str', 'empty'):
				pre = headers[0][i]
				post = ''
			if types == ('empty', 'empty'):
				pre = ''
				post = ''

			new_header.append(pre + post)
			i += 1

		keepRows.insert(0,new_header)

	return keepRows


def removeEmptyColumns(keepRows):
	#----------------------------------------------
	#  remove empty columns
	#  To Do: do this more efficiently!!
	header = keepRows[0]

	# find any empty header cells
	emptyHeaderCells = []
	i = 0
	for cell in header:
		if(getType(cell) == 'empty'):
			emptyHeaderCells.append(i)
		i += 1

	# check if all the data cells in column are also empty
	columns_to_remove = []
	for col in emptyHeaderCells:
		remove_col = True
		for row in keepRows:
			if getType(row[col]) != 'empty':
				remove_col = False
		if remove_col == True:
			columns_to_remove.append(col)

	# # Now go through and remove columns from header and data
	cleanRows = []
	for row in keepRows:
		tempRow = []
		i=0
		for elem in row:
			if i not in columns_to_remove:
				tempRow.append(elem)
			i+=1
		cleanRows.append(tempRow)

	return cleanRows


def possibleSumsRow(row):
	sumsTypes = ['num', 'empty']
	for cell in row:
		if getType(cell) not in sumsTypes:
			return False
	return True


def removeSumsRow(rows):
	# assumption: have already removed any additional summary table
	# assumption: the last row is either data, or contains sums of some columns

	row_y = rows[len(rows)-2]
	row_z = rows[len(rows)-1]

	# print row_y, getTypesPattern(row_y)
	# print row_z, getTypesPattern(row_z)


	# ToDo make this more robust!!! Check previous rows...
	if possibleSumsRow(row_z):
		rows = rows[:-1]


	return rows


def saveAsCSV(cleanRows, dest_folder, file_name_short):
	complete_name = os.path.join(dest_folder, file_name_short + '_cleaned.csv')
	with open( complete_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerows(cleanRows)

	f.close()

# ---------------------------------------------------------------------------------------
def cleanFile(file_name, dest_folder, top=False):


	if top:
		#ToDo: add controls to trigger removal of extra rows at top of file
		print '-->remove extra rows at top of this csv'


	file_path = file_name
	file_name = os.path.basename(file_name)
	file_name_short = os.path.splitext(file_name)[0]


	# not sure if this is good idea....might use up memory
	rows = getRows(file_path)

	#converting an excel sheet to csv may result in empty cells of first row to be filled with 'Unnamed: #'
	rows = cleanUnnamed(rows)

	# need to remove empty columns before getting type patterns....could have lots of empty columns 
	rows = removeEmptyColumns(rows)


	common_row_patterns = getRowTypePatterns(rows)
	# for row in common_row_patterns:
	# 	print row
	
	# most common length should be our data rows 
	counts = getCommonRowLengths(rows) #Counter(row_lengths)
	common_row_length = counts.most_common(1)[0][0]

	rows = removeEmptyRows(rows)

	# Only execute this if command line argument 'top' is used
	if top:
		rows = removeExtraTopRows(rows, common_row_length)


	rows = flattenHeaders(rows)

	rows = removeSummaryTable(rows, common_row_length)

	# any extra tables must be already removed by now
	rows = removeSumsRow(rows)

	for row in rows:
		print row
	
	saveAsCSV(rows, dest_folder, file_name_short)

	# this is just for testing
	# print '-------------------------------------'
	# for row in rows:
	# 	print row
#--------------------------------------------------------------------------------------------






