#! python3
# 
# NAME         : find_huge_files.py
#
# DESCRIPTION  : Walks through a folder tree and searches for exceptionally
#                big files (i.e. ones whose size > 100MB). Displays their
#                main info. Deletes them if `delete` kwarg is set to `True`.
#
# AUTHOR       : Tim Kornev (@Timmate on GitHub)
#
# CREATED DATE : 7th of August, 2016
#


import os


FOLDERS = []    # folders to search in
MAX_SIZE = 100000000    # maximum allowed size of files (in bytes)


def find_huge_files(folder, max_size, delete=False):
    print()
    if delete:
        print('DELETE MODE.')
    print('FOLDER: {}'.format(folder))
    print()

    # Walk recursively down the folder.
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            try:
                filepath = os.path.join(foldername, filename)
                filesize = os.path.getsize(filepath)
                if filesize > max_size:
                    # Found a huge file. Display properties info.
                    filesize = round(filesize / 1000000)    # display size in MB
                    print('Name: {}'.format(filename))
                    print('Size: {}MB'.format(filesize))
                    print('Path: {}'.format(filepath))
                    print()
                    if delete:
                        os.remove(filename)
                    
            except FileNotFoundError:
                continue

# Search in specified folders.
for folder in FOLDERS:
    # Set `delete` kwarg to `True` to delete huge files.
    find_huge_files(folder, MAX_SIZE)   

print('Done.')
print()
