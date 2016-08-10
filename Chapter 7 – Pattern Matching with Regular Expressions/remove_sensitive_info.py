#! python3
#
# NAME         : remove_sensitive_info.py
#
# DESCRIPTION  : Removes sensitive information such as Social Security
#                or credit card numbers from the clipboard.
#
# AUTHOR       : Tim Kornev (@Timmate on GitHub)
#
# CREATED DATE : 6th of August, 2016


import re

import pyperclip


# Assume that credit card number is formatted like this: XXXX XXXX XXXX XXXX
# and Social Security number is formatted like this: XXX-XX-XXXX
credit_card_number_regex = re.compile(r'\d{3}-\d{2}-\d{4}')
social_secirity_number_regex = re.compile(r'\d{4} \d{4} \d{4} \d{4}')

# Copy the text from the clipboard.
text = pyperclip.paste()

# Remove the sensetive information.
text = credit_card_number_regex.sub('', text)
text = social_security_number_regex.sub('', text)

# Copy the result text to the clipboard.
pyperclip.copy(text)

print()
print('Done.')
print()
