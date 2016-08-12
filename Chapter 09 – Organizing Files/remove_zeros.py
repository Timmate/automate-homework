#! python3
# 
# NAME         : remove_zeros.py
#
# DESCRIPTION  : Changes zero-padded files' names to non-zero-padded ones.
#
# AUTHOR       : Tim Kornev (@Timmate on GitHub)
#
# CREATED DATE : 7th of August, 2016
#


import os
import shutil
import re


# Set extensions of files whose names should be changed.
EXTENSIONS = ['.txt']


# Set regex that matches only zero-padded files' names.
filename_regex = re.compile(r'''
                            ^                 
                            ([a-zA-Z1-9]+)    # main part 
                            (0+)              # zeros part
                            (\d+)             # after-zeros-digits part
                            (\.\w{2,4})       # extension part
                            $                 
                            ''', re.VERBOSE)

for filename in os.listdir('.'):
    for extension in EXTENSIONS:
        # Rename only those files that have zero-padded name and one of the
        # specified extensions.
        if filename.endswith(extension) and filename_regex.search(filename):
            # Set non-zero-padded filename.
            mo = filename_regex.search(filename)
            main_part = mo.group(1)
            after_zeros_digits_part = mo.group(3)
            extension_part = mo.group(4)

            new_filename = main_part + after_zeros_digits_part + extension_part

            # Display process information.
            print('Renaming {} to {}...'.format(filename, new_filename))

            # Find absolute filenames (paths to the files) that `shutil`
            # can use.
            filename = os.path.abspath(filename)
            new_filename = os.path.abspath(new_filename)

            # Rename the file.
            shutil.move(filename, new_filename)

print()    
print('Done.')
print()
            
            
