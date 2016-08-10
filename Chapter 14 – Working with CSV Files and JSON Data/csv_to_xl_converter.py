#! python3
#
# NAME         : csv_to_xl_converter.py
#
# DESCRIPTION  : Converts each CSV file in current working directory to an Excel
#                spreadsheet.
#
# AUTHOR       : Tim Kornev (@Timmate on GitHub)
#
# CREATED DATE : 9th of July, 2016
#


import os
import csv

import openpyxl


SAVE_DIR = 'converted_csv_files'


os.makedirs(SAVE_DIR, exist_ok=True)

print()
print('SAVE CONVERTED FILES IN: {}'.format(SAVE_DIR))

for filename in os.listdir('.'):
    # Read in CSV files.    
    if filename.endswith('.csv'):
        print('Reading in {}...'.format(filename))
        f = open(filename)
        csv_reader = csv.reader(f)
        contents = list(csv_reader)
        line_num = csv_reader.line_num
        f.close()

        # Write data to an Excel workbook file.
        wb = openpyxl.Workbook()
        sheet = wb.active

        for row in range(1, line_num + 1):
            number_of_columns = len(contents[row - 1])
            for col in range(1, number_of_columns + 1):
                sheet.cell(row=row, column=col).value = contents[row - 1][col - 1]

        # Save result in an Excel spreadsheet.
        xl_filename = filename.split('.')[0] + '.xlsx'
        print('Saving converted CSV file as {}...'.format(xl_filename))
        xl_filename = os.path.join(SAVE_DIR, xl_filename)
        wb.save(xl_filename)

print()
print('Done.')
print()
