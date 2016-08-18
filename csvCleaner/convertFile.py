import os
import pandas as pd 

def xlsToCsv(filename, dest_folder):
	print filename

	file_name = os.path.basename(filename)
	file_name_short = os.path.splitext(file_name)[0]
	file_path = os.path.join(dest_folder, file_name_short + '.csv')
	data_xls = pd.read_excel(filename, index_col=None)
	data_xls.to_csv(file_path, encoding='utf-8')
	return file_path
