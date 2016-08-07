#! python3
#
# NAME         : txt_search.py
#
# DESCRIPTION  : Opens all text files in the current working directory and
#                looks for any text that matches a regex pattern given by
#                the user. 
#
# AUTHOR       : Tim Kornev (Timmate profile on GitHub)
#
# CREATED DATE : 4th of July, 2016
#


import os
import re


os.chdir('txt_search_test')
 
# Take the user's input to create regex pattern.
print()
regex_pattern = input('Enter a regex pattern: ')
regex = re.compile(regex_pattern)

# Read in each '.txt' file in the current working directory and use the regex
# pattern to find matches.
matches = []
for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        read_file = open(filename)  
        contents = read_file.read()
        read_file.close()
        mo = regex.findall(contents)    # 'mo' stands for Match objects
        if mo:
            matches.append((mo, filename,))     

print()        
if matches:
    for match in matches:
        print("{} matched search pattern in '{}' file.".format(match[0], match[1]))
else:
    print('No matches found. ')
    
print()
print('Done.')
print()
