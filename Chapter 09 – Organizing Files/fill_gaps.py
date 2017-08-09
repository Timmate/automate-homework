#! python3
# 
# NAME         : fill_gaps.py
#
# DESCRIPTION  : Fills in gaps in sequences of files in the current working directory.
#
# AUTHOR       : Tim Kornev (@Timmate on GitHub)
#
# CREATED DATE : 9th of August, 2017
#


import re
import os
import shutil


START_FROM_ZERO = False

PREFIX = 'spam'
NUMBER_OF_DIGITS = 3
EXTENSION = '.txt'

MASK = re.compile(r'%s\d{%i}%s' % (PREFIX, NUMBER_OF_DIGITS, EXTENSION))


print('DIR: {}'.format(os.getcwd()))
print('MASK: {}{}{}'.format(PREFIX, '\d' * NUMBER_OF_DIGITS, EXTENSION))
print()

# Find all files using the mask.
filenames = list(filter(lambda filename: MASK.findall(filename), os.listdir()))

if not filenames:
    print('No files found.')

else:
    filenames.sort()

    if START_FROM_ZERO:
        new_index = 0
        
    else:
        # Start from index of the first file.
        match = re.search(r'%s(\d{%i})%s' % (PREFIX, NUMBER_OF_DIGITS, EXTENSION), filenames.pop(0))
        new_index = int(match.group(1)) + 1

    for filename in filenames:
        new_filename = '%s%0.{}i%s'.format(NUMBER_OF_DIGITS) % (PREFIX, new_index, EXTENSION)

        if filename != new_filename:
            print('Renaming {} to {}...'.format(filename, new_filename))
            shutil.move(filename, new_filename)
            
        else:
            print('Exists: {}'.format(filename))

        new_index += 1
              
print()
print('Done.')
    


    
    
