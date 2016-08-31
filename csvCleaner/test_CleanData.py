import unittest
from cleanData import getColumn, nibble, getType, getTypesPattern, isColNumerical




class CleaningTestCase(unittest.TestCase):
	
	def test_getColumn(self):

		matrix = [[1,2,3,4],
				 [11,22,33,44],
				 [111, 222, 333, 444]]

		i = 1
		col = [2, 22, 222]

		self.assertEqual(getColumn(matrix, i), col)



	def test_nibble(self):
		# testing nibble(row)
		print 'write test for nibble(row)'


	def test_getType(self):

		nums = [5, 5.5, -5, '5']

		for num in nums: 
			self.assertEqual(getType(num), 'num')
			self.assertNotEqual(getType(num), 'str')

		empties = ['', ' ']
		for empt in empties:
			self.assertEqual(getType(empt), 'empty')
			self.assertNotEqual(getType(empt), 'str')


	def test_getTypesPattern(self):
		#getTypesPattern(row)

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

		col = [1,2,3,4]
		self.assertEqual(isColNumerical(col), True)

		col = [1.2, 2, 3, 4]
		self.assertEqual(isColNumerical(col), True)

		col = ['one', 2, 3, 'four']
		self.assertNotEqual(isColNumerical(col), True)

		

	def test_isRowEmpty(self):
		#testing isRowEmpty(pattern)
		pass

	def test_isInRanges(self):
		#tesst isInRanges(i, ranges)
		pass

	def test_getLimitedRows(self):
		#testing getLimitedRows(rows, rownums)
		pass

	def test_getRows(self):
		#testing getRows(file_path)
		pass


	def test_getColumns(self):
		#testing getColumns(rows, columns)
		pass
	
	def test_cleanUnnamed(self):
		#testing cleanUnnamed(rows)
		pass



	def test_getRowTypePatterns(self):
		# getRowTypePatterns(rows)
		pass

	def test_getCommonRowLengths(self):
		# getCommonRowLengths(rows)
		pass

	def test_removeEmptyRows(self):
		# removeEmptyRows(rows)
		pass

	def test_removeExtraTopRows(self):
		# removeExtraTopRows(rows, common_row_length)
		pass


	def test_removeSummaryTable(self):
		#removeSummaryTable(rows, common_row_length)
		pass


	def test_removeEmptyFromList(self):
		# removeEmptyFromList(list)
		pass


	def test_getHeaderNameFromData(self):
		# getHeaderNameFromData(rows, i)
		pass


	def test_flattenHeaders(self):
		# flattenHeaders(keepRows)
		pass


	def test_removeEmptyColumns(self):
		# removeEmptyColumns(keepRows)
		pass


	def test_possibleSumsRow(self):
		# possibleSumsRow(row)
		pass

	def  test_removeSumsRow(self):
		# removeSumsRow(rows)
		pass

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