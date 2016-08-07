#! python3
#
# NAME         : password_validator.py
#
# DESCRIPTION  : Ensures that a password is strong.
#
# AUTHOR       : Tim Kornev (Timmate profile on GitHub)
#
# CREATED DATE : 7th of August, 2016


import re


lowercase_regex = re.compile(r'[a-z]')  
uppercase_regex = re.compile(r'[A-Z]')
digit_regex = re.compile(r'\d')

def password_validator(password):
    lowercase_mo = lowercase_regex.search(password)
    uppercase_mo = uppercase_regex.search(password)
    digit_mo = digit_regex.search(password)

    if len(password) >= 8 and lowercase_mo and uppercase_mo and digit_mo:
        return True
    else:
        return False
