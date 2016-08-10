#! python3
#
# NAME         : imgur_searcher.py
#
# DESCRIPTION  : Opens several web pages on Imgur.com with searching results for
#                command line arguments.
#
# AUTHOR       : Tim Kornev (@Timmate on GitHub)
#
# CREATED DATE : 7th of July, 2016
#


import sys
import webbrowser as wb

import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


print()
print('Searching images on Imgur...')

URL = 'https://imgur.com'
   
search_for = ' '.join(sys.argv[1:])

# Download the page.
res = requests.get('{}/search/score?q={}'.format(URL, search_for))
try:
    res.raise_for_status()
except HTTPError as err:    # catch HTTP 404 error message
    print('Oops! An error occured: {}'.format(str(err)))

# Parse the HTML.
soup = BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('.image-list-link')
      
number_of_links = min(5, len(link_elems))   # should open 5 links or less.

# Open links.
for i in range(number_of_links):
    link_to_image = link_elems[i].get('href')
    wb.open('{}{}'.format(URL, link_to_image))

print()    
print('Done.')
print()
