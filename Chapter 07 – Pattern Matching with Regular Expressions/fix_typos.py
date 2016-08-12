#! python3
#
# NAME         : fix_typos.py
#
# DESCRIPTION  : Finds and fixes common typos such as   multiple   spaces
#                between words, accidentally accidentally repeated words,
#                or multiple exclamation marks at the end of sentences.
#                Those are annoying!! Uses the text from the clipboard.
#
# AUTHOR       : Tim Kornev (@Timmate on GitHub)
#
# CREATED DATE : 6th of August, 2016
#


import re

import pyperclip


# Set regex for typos.
exclamation_marks_regex = re.compile(r'!{2,}')
multiple_spaces_regex = re.compile(r'\s{2,}')
repeated_words_regex = re.compile(r'\b(\w+)\s+\1\b')

# Paste text from the clipboard.
text = pyperclip.paste()

# Fix typos.
text = exclamation_marks_regex.sub('!', text)
text = multiple_spaces_regex.sub(' ', text)
text = repeated_words_regex.sub(r'\1', text)

# Copy the result text to the clipboard.
pyperclip.copy(text)

print()
print('Done.')
print()
