import unittest
from cleanData import getType, getTypesPattern




class CleaningTestCase(unittest.TestCase):
	# Tests for things

	def test_get_type(self):

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
		row_types = ['str', 'num', 'num', 'num', 'num']
		self.assertNotEqual(getTypesPattern(row), row_types)




if __name__ == '__main__':
    unittest.main()