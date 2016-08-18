import os
import pandas as pd 


def checkFileType(filename, dest_folder):

	ext= os.path.splitext(filename)[1]

	if ext == '.xls':
		csv_path = xlsToCsv(filename, dest_folder)
		return csv_path

	elif ext == '.csv':
		return filename #os.path.join(dest_folder, filename)

	else: 
		return 'Error, this file type not accepted'


def xlsToCsv(filename, dest_folder):

	file_name = os.path.basename(filename)
	file_name_short = os.path.splitext(file_name)[0]
	new_file_path = os.path.join(dest_folder, file_name_short + '.csv')

	data_xls = pd.read_excel(filename, index_col=None)
	data_xls.to_csv(new_file_path, encoding='utf-8')
	return new_file_path
