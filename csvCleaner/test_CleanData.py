import unittest
# from cleanData import getColumn, nibble, getType, getTypesPattern, isColNumerical, isRowEmpty, isInRanges
from cleanData import *




class CleaningTestCase(unittest.TestCase):
	
	def test_getColumn(self):
		# getColumn(matric, i)

		matrix = [[1,2,3,4],
				 [11,22,33,44],
				 [111, 222, 333, 444]]

		i = 1
		col = [2, 22, 222]

		self.assertEqual(getColumn(matrix, i), col)



	def test_nibble(self):
		# nibble(row)
		print 'ToDo: write test for nibble(row)'


	def test_getType(self):
		# getType(elem)

		nums = [5, 5.5, -5, '5']

		for num in nums: 
			self.assertEqual(getType(num), 'num')
			self.assertNotEqual(getType(num), 'str')

		empties = ['', ' ']
		for empt in empties:
			self.assertEqual(getType(empt), 'empty')
			self.assertNotEqual(getType(empt), 'str')


	def test_getTypesPattern(self):
		# getTypesPattern(row)

		row = ['one', 'two', 3,'' ,'five', 6.6]
		row_types = ['str', 'str', 'num', 'empty', 'str', 'num']
		self.assertEqual(getTypesPattern(row), row_types)

		row = [1,2,3,4,5]
		row_types = ['num', 'num', 'num', 'num', 'num']
		self.assertEqual(getTypesPattern(row), row_types)

		row = [1.1,0.2,3,4,5]
		row_types = ['num', 'num', 'num', 'num', 'num']
		self.assertEqual(getTypesPattern(row), row_types)

		row = [1,2,3,4,5]
		row_types = ['str', 'num', 'num', 'num', 'num']
		self.assertNotEqual(getTypesPattern(row), row_types)


	

	def test_isColNumerical(self):
		# isColNumerical(col)

		col = [1,2,3,4]
		self.assertEqual(isColNumerical(col), True)

		col = [1.2, 2, 3, 4]
		self.assertEqual(isColNumerical(col), True)

		col = ['one', 2, 3, 'four']
		self.assertNotEqual(isColNumerical(col), True)

		

	def test_isRowEmpty(self):
		# isRowEmpty(pattern)
		
		pattern = ['empty', 'empty']
		self.assertEqual(isRowEmpty(pattern), True)

		pattern = ['empty', 'empty', 'str']
		self.assertNotEqual(isRowEmpty(pattern), True)


	def test_isInRanges(self):
		#  isInRanges(i, ranges)
		i = 1

		ranges = [1]
		self.assertEqual(isInRanges(i, ranges), True)

		ranges = [1,2]
		self.assertEqual(isInRanges(i, ranges), True)

		ranges = ['0-3']
		self.assertEqual(isInRanges(i, ranges), True)

		ranges = ['0-3', 5]
		self.assertEqual(isInRanges(i, ranges), True)

		i = 99
		ranges = ['0-3', 5]
		self.assertNotEqual(isInRanges(i, ranges), True)

		i = -1
		ranges = ['0-3']
		self.assertNotEqual(isInRanges(i, ranges), True)



	def test_getLimitedRows(self):
		# getLimitedRows(rows, rownums)
		
		print 'ToDo: write test for getLimitedRows(rows, rownums)'

	def test_getRows(self):
		# getRows(file_path)
		print 'ToDo: write test for getRows(file_path)'


	def test_getColumns(self):
		# getColumns(rows, columns)
		print 'ToDo: write *more* tests for getColumns(rows, columns)'
		
		rows = [[1,2,3,4],
				[11,22,33,44],
				[111, 222, 333, 444]]

		columns = [1]
		new_rows = [[2],
					[22],
					[222]]

		self.assertEqual(getColumns(rows, columns), new_rows)


	
	def test_cleanUnnamed(self):
		# cleanUnnamed(rows)
		
		rows = [['one', 'two', 'Unnamed_1'],
				[1,2,3]]

		new_rows =[['one', 'two', ''],
				[1,2,3]]

		self.assertEqual(cleanUnnamed(rows), new_rows)


	def test_getRowTypePatterns(self):
		# getRowTypePatterns(rows)
		# getting most common patterns, in order of frequency, with most frequent first
		print 'ToDo: write more tests for getRowTypePatterns(rows)'
		
		rows = [[1, 2, 'three', ''],
				[11,22,33,44],
				[111, 222, 333, 444]]
		patterns = [(('num', 'num', 'num', 'num'), 2),
					(('num', 'num', 'str', 'empty'), 1)]

		self.assertEqual(getRowTypePatterns(rows), patterns)


	def test_getCommonRowLengths(self):
		# getCommonRowLengths(rows)
		rows = [[1, 2, 'three', ''],
				[11,22,33,44],
				[111, 222, 333, 444]]
		lengths = {4: 3}

		self.assertEqual(getCommonRowLengths(rows), lengths)


		rows = [[1, 2, 'three'],
				[11,22,33,44],
				[111, 222, 333, 444]]
		lengths = {4: 2, 3: 1}

		self.assertEqual(getCommonRowLengths(rows), lengths)



	def test_removeEmptyRows(self):
		# removeEmptyRows(rows)
		rows = [[1, 2, 'three'],
				[11,22,33,44],
				['','','',''],
				[111, 222, 333, 444]]

		new_rows = rows = [[1, 2, 'three'],
				[11,22,33,44],
				[111, 222, 333, 444]]


		self.assertEqual(removeEmptyRows(rows), new_rows)



	def test_removeExtraTopRows(self):
		# removeExtraTopRows(rows, common_row_length)
		rows = [['extra'],
				['one', 'two', 'three', 'four', 'five', 'six'],
				[11,22,33,44, 55, 66],
				[111, 222, 333, 444, 555, 666]]

		common_row_length = 6		

		new_rows = rows = [['one', 'two', 'three', 'four', 'five', 'six'],
				[11,22,33,44, 55, 66],
				[111, 222, 333, 444, 555, 666]]

		self.assertEqual(removeExtraTopRows(rows, common_row_length), new_rows)


		lengths = getCommonRowLengths(rows)
		common_row_length = lengths.most_common(1)[0][0]

		self.assertEqual(removeExtraTopRows(rows, common_row_length), new_rows)



	def test_removeSummaryTable(self):
		#removeSummaryTable(rows, common_row_length)
		print "ToDo: write test for removeSummaryTable(rows, common_row_length)"


	def test_removeEmptyFromList(self):
		# removeEmptyFromList(list)
		list = ['one', 'two', '', 'four']
		new_list = list = ['one', 'two', 'four']

		self.assertEqual(removeEmptyFromList(list), new_list)
		self.assertEqual(len(removeEmptyFromList(list)), len(new_list))



	def test_getPossibleHeaderNamesFromData(self):
		# getPossibleHeaderNamesFromData(rows, i)
		rows = [['one', '', 'three', '', '', 'six'],
				[11, '', 33, 'four', 55, 66],
				[11, '', 33, 'four', 55, 66],
				[111, '', 333, 'two', 555, 666]]

		self.assertEqual(getPossibleHeaderNamesFromData(rows, 3), ['two', 'four'])
		self.assertEqual(getPossibleHeaderNamesFromData(rows, 4), ['num_4', 555, 55])
		self.assertEqual(getPossibleHeaderNamesFromData(rows, 1), [])


	


	def test_getHeaderNameFromData(self):
		# getHeaderNameFromData(rows, i)
		rows = [['one', '', 'three', '', '', 'six'],
				[11, '', 33, 'four', 55, 66],
				[11, '', 33, 'four', 55, 66],
				[111, '', 333, 'two', 555, 666]]

		self.assertEqual(getHeaderNameFromData(rows, 3), 'two')
		self.assertEqual(getHeaderNameFromData(rows, 4), 'num_4')
		self.assertEqual(getHeaderNameFromData(rows, 1), '')


	def test_flattenHeaders(self):
		# flattenHeaders(keepRows)
		print 'ToDo: write test for flattenHeaders(rows)'


	def test_removeEmptyColumns(self):
		# removeEmptyColumns(keepRows)
		rows = [['one', 'two', 'three', 'four', '', 'six'],
				[11,22,33,44,' ' , 66],
				[111, 222, 333, 444,' ' , 666]]

		new_rows = [['one', 'two', 'three', 'four', 'six'],
				[11,22,33,44, 66],
				[111, 222, 333, 444, 666]]

		self.assertEqual(removeEmptyColumns(rows), new_rows)



		rows = [['one', 'two', 'three', ' ', 'five', 'six'],
				[11,22,33,44,' ' , 66],
				[111, 222, 333, 444,' ' , 666]]

		new_rows = [['one', 'two', 'three', 'five', 'six'],
				[11,22,33,44, 66],
				[111, 222, 333, 444, 666]]

		self.assertNotEqual(removeEmptyColumns(rows), new_rows)



	def test_possibleSumsRow(self):
		# possibleSumsRow(row)
		row = ['one', 'two', 'three', 'four']
		self.assertEqual(possibleSumsRow(row), False)

		row = [1,2, '', '', '', 3]
		self.assertEqual(possibleSumsRow(row), True)


	def  test_removeSumsRow(self):
		# removeSumsRow(rows)
		rows = [['one', 'two', 'three', 'four', 'five'],
				[1, 2, 3, 4, 5,],
				[11, 22, 33, 44, 55],
				[111, 222, 333, 444, 555],
				['', '', 3333, '', 5555]]

		new_rows = [['one', 'two', 'three', 'four', 'five'],
				[1, 2, 3, 4, 5,],
				[11, 22, 33, 44, 55],
				[111, 222, 333, 444, 555]]

		self.assertEqual(removeSumsRow(rows), new_rows)



	def test_saveAsCSV(self):
		# def saveAsCSV(cleanRows, dest_folder, file_name_short)
		pass

	def test_saveAsJSON(self):
		# saveAsJSON(rows, dest_folder, file_name_short)
		pass

	def test_saveAsJSON_2(self):
		# saveAsJSON_2(rows, dest_folder, file_name_short)
		pass


	def test_cleanFile(self):
		# cleanFile(file_name, dest_folder, skim=False, columns=[], rownums=[], json=False, json2=False)
		pass




if __name__ == '__main__':
    unittest.main()