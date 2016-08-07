#! python3
#
# NAME         : strip_with_re.py
#
# DESCRIPTION  : The regex analog of the `strip()` Python built-in function.
#
# AUTHOR       : Tim Kornev (Timmate profile on GitHub)
#
# CREATED DATE : 7th of August, 2016


import re


def strip(string, char=' '):
    regex = re.compile(r'''
                       ^        # beginning
                       [{}]*    # left *char* part
                       (.*?)    # the "core" of the string
                       [{}]*    # right *char* part
                       $        # end
                       '''.format(char, char), re.VERBOSE)
    
    mo = regex.search(string)
    
    if mo:
        return mo.group(1)  # return the "core" of the string
    else:
        return None

    
