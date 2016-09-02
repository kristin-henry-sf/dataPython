from __future__ import division
import os
import csv, json
import numbers
# import pandas as pd
from collections import Counter



def getColumn(matrix, i):
	return [row[i] for row in matrix]


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
		elem = elem.strip()
		if elem == '':
			return 'empty'
	return 'str'


def getTypesPattern(row):
	row_types = []
	for elem in row:
		row_types.append(getType(elem))
	return row_types


def isColNumerical(col):
	for elem in col:
		if getType(elem) != 'num':
			return False
	return True 

def isRowEmpty(pattern):
	for elem in pattern:
		if elem != 'empty':
			return False
	return True

def isInRanges(i, ranges):
	# originally written to compare value to commandline args, which are passed as strings
	
	for r in ranges:
		r = str(r) # this is for testing, and using,  outside of command line
		r = r.replace(',', '')
		if '-' in r:
			nums = r.split('-')
			if float(i) >= float(nums[0]) and float(i) <= float(nums[1]):
				return True
		else:
			if float(i) == float(r):
				return True
	
	return False
			

def getLimitedRows(rows, row_nums):
	if '-' in row_nums:
		nums = row_nums.split('-')
		min = int(nums[0])
		max = int(nums[2])
	else:
		min = 0
		max = int(row_nums[0])

	rows = rows[min:max]

	return rows


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
	

def getColumns(rows, columns):
	#ToDo: this is not efficient....look for better ways
	new_rows = []

	for row in rows:
		i = 0
		new_row = []
		for elem in row:
			if isInRanges(i, columns):
				new_row.append(elem)
			i+=1

		new_rows.append(new_row)

	return new_rows


def cleanUnnamed(rows):
	row = rows[0] 	# get the first row, only one that could have 'Unnamed: # ' cells
	rows = rows[1:] # save the rest of the rows
	
	new_row = []
	for cell in row:
		if 'Unnamed' in cell:
			new_row.append('')
		else:
			new_row.append(cell)
	rows.insert(0, new_row) # put our cleaned row back as first row 
	
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
		if len(row) >= common_row_length/2:
			break
	return rows[:i+1]


def removeEmptyFromList(list):
	new_list = []
	for l in list:
		if l != '':
			new_list.append(l)
	return new_list


def getPossibleHeaderNamesFromData(rows, i):
	# might want to add a command line interface for selecting among possible header names,
	# so abstracting this code which will pass the names to getHeaderNameFromData 
	
	col_data = set(getColumn(rows, i))
	col_data = removeEmptyFromList(col_data) 

	if len(col_data)> 0:
		if isColNumerical(col_data):
			col_data.insert(0, 'num_' + str(i))
		else:
			col_data.sort(key=len)

	return col_data


def getHeaderNameFromData(rows, i):
	# get shortest name from data in column. If no data, then this is empty column and no header needed
	h_name = ''

	col_data = getPossibleHeaderNamesFromData(rows, i)

	if len(col_data) > 0:
		h_name = col_data[0]

	return h_name


def flattenHeaders(rows):
	# This is not as robust as it can be, keeping it simple for now
	# Assumption: first rows are likely to be headers, and when pattern becomes 'common', it's data
	# Assumption: headers will not have numbers as names --> header rows don't have number types in them
	headers = []
	for row in rows[:2]:
		if 'num' not in getTypesPattern(row):
			headers.append(row)
		else:
			break

	if len(headers) > 1:
		# remove the old headers 
		rows = rows[len(headers):]

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
				post = '****' + getHeaderNameFromData(rows,i)[:9]  # the '****' indicates header name was extracted and needs to be edited by a person
				# print 'extracted Header: ', post

			new_header.append(pre + post)
			i += 1

		rows.insert(0,new_header)

	return rows


def removeEmptyColumns(rows):
	#----------------------------------------------
	#  remove empty columns
	#  To Do: do this more efficiently!!
	header = rows[0]

	# find any empty header cells
	empty_header_cells = []
	i = 0
	for cell in header:
		if(getType(cell) == 'empty'):
			empty_header_cells.append(i)
		i += 1

	# check if all the data cells in column are also empty
	columns_to_remove = []
	for col in empty_header_cells:
		remove_col = True
		for row in rows:
			if getType(row[col]) != 'empty':
				remove_col = False
		if remove_col == True:
			columns_to_remove.append(col)

	# # Now go through and remove columns from header and data
	clean_rows = []
	for row in rows:
		temp_row = []
		i=0
		for elem in row:
			if i not in columns_to_remove:
				temp_row.append(elem)
			i+=1
		clean_rows.append(temp_row)

	return clean_rows


def possibleSumsRow(row):
	sums_types = ['num', 'empty']
	for cell in row:
		if getType(cell) not in sums_types:
			return False
	return True


def removeSumsRow(rows):
	# assumption: have already removed any additional summary table
	# assumption: the last row is either data, or contains sums of some columns
	row_y = rows[len(rows)-2]
	row_z = rows[len(rows)-1]

	# ToDo make this more robust!!! Check previous rows...
	if possibleSumsRow(row_z):
		rows = rows[:-1]

	return rows


def saveAsCSV(rows, dest_folder, file_name_short):
	complete_name = os.path.join(dest_folder, file_name_short + '_cleaned.csv')
	with open( complete_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerows(rows)

	f.close()


def saveAsJSON(rows, dest_folder, file_name_short):
	# this needs improvements
	complete_name = os.path.join(dest_folder, file_name_short + '_cleaned.json')
	data = []

	headers = rows[0]
	for row in rows[1:]:
		d = {}
		i =0
		for elem in headers:
			d[elem] = row[i]
			i+=1
		data.append(d)

	with open(complete_name, 'w') as f:
		json.dump(data, f)


def saveAsJSON_2(rows, dest_folder, file_name_short):
	# Assumption: second header row is nested under the first. Not always a safe assumption, may need user intervention.

	print "saving as nested json, without flattening headers"

	# this needs improvements
	complete_name = os.path.join(dest_folder, file_name_short + '_cleaned.json')
	data = []

	subheaders = rows[1] # get second row of headers

	for row in rows[2:]:
		d = {}
		i =0
		parent = None
		for elem in row:

			if rows[0][i] != '':
				parent = rows[0][i]
				d[parent] = {}
				#ToDo: if subheader is empty, extract header from column data---should do this before looping through rows

			d[parent][subheaders[i]] = row[i]
			i+=1
		
		data.append(d)

	# print data

	with open(complete_name, 'w') as f:
		json.dump(data, f)



# ---------------------------------------------------------------------------------------
def cleanFile(file_name, dest_folder, skim=False, columns=[], rownums=[], json=False, json2=False):

	file_path = file_name
	file_name = os.path.basename(file_name)
	file_name_short = os.path.splitext(file_name)[0]


	rows = getRows(file_path)

	#converting an excel sheet to csv may result in empty cells of first row to be filled with 'Unnamed: #'
	rows = cleanUnnamed(rows)

	# could have lots of empty columns 
	rows = removeEmptyColumns(rows)


	# get data type patterns from data in rows
	common_row_patterns = getRowTypePatterns(rows)
	counts = getCommonRowLengths(rows) 
	common_row_length = counts.most_common(1)[0][0] #most common length should be our data rows 


	# Only execute this if command line argument 'top' is used
	if skim:
		print 'skim of the top'

		rows = removeExtraTopRows(rows, common_row_length)


	rows = removeEmptyRows(rows)

	if not json2:
		# some files have nested headers, we want just one row of header names
		rows = flattenHeaders(rows)

	# some files have summary tables below all the actual data 
	rows = removeSummaryTable(rows, common_row_length)

	#any extra tables must be already removed by now
	rows = removeSumsRow(rows)

	# make sure we take all columns and rows if not indicated otherwise
	if len(rownums) >0:
		rows = getLimitedRows(rows, rownums)
	if len(columns) >0:
		rows = getColumns(rows, columns)

	if json:
		saveAsJSON(rows, dest_folder, file_name_short)
	elif json2:
		saveAsJSON_2(rows, dest_folder, file_name_short)
	else:
		saveAsCSV(rows, dest_folder, file_name_short)

	#this is just for testing
	# print '-------------------------------------'
	# for row in rows:
	# 	print row
#--------------------------------------------------------------------------------------------






