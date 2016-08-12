#! python3
#
# NAME         : urls_grabber.py
#
# DESCRIPTION  : Looks for URLs in the clipboard. 
#
# AUTHOR       : Tim Kornev (@Timmate on GitHub)
#
# CREATED DATE : 4th of July, 2016

# Copy these strings to the clipboard and run the script to test it:

# htp:/facebook.com
# http://192.ru
# https://www.imgur.com
# http://google.com
# https://pypi.python.org/pypi/pyperclip
# http://pyperclip.readthedocs.io/en/latest/introduction.html


import re

import pyperclip


text = pyperclip.paste()    # if you use Linux OS, the error raises here

url_regex = re.compile(r'''(
    http                # "http" beginning
    s?                  # "s" is "Security"!
    \:\/\/              # ://
    (www\. | .+)?       # "www." or something else (optional)
    [a-z]+              # domain (only Latin letters)
    \.[a-z]{2,4}        # top-level domain (".smth") (2-4 letters)
    (\/.+)?             # end parts of the url (optional)
    )''', re.VERBOSE)

urls = (url_regex.findall(text))
print()
if urls:
    print('URLs: ')
    for url in urls:
        print('\t' + url[0])   # print the whole url
else:
    print('Found no URLs. :(')
    
print()
print('Done.')
print()          
