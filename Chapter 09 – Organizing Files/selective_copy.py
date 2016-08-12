#! python3
# 
# NAME         : selective_copy.py
#
# DESCRIPTION  : Walks through a folder tree and searches for files with
#                specified file extensions. Copies them to a new folder.
#                NOTE: It copies just files, not folders that contain files.
#
# AUTHOR       : Tim Kornev (@Timmate on GitHub)
#
# CREATED DATE : 4th of July, 2016
#


import os
import shutil


WORK_DIR = '/home/tim/Tim/Programming/Code/Python'
SAVE_DIR = '/home/tim/Desktop/wtf'

EXTENSIONS = ['.py', '.xlsx']


os.makedirs(SAVE_DIR, exist_ok=True)
    
print()
print("COPY FROM: {}".format(WORK_DIR))
print("SAVE TO: {}".format(SAVE_DIR))
print("EXTENSIONS: {}".format(str(EXTENSIONS)))
print()          

for foldername, subfolders, filenames in os.walk(WORK_DIR):
    for filename in filenames:
        for extension in EXTENSIONS:    # yes, triple `for` loop
            if filename.lower().endswith(extension):
                    print("Copying {}...".format(filename))
                    filename = os.path.join(foldername, filename)
                    shutil.copy(filename, SAVE_DIR)
                    
print()
print('Done.')
print()
