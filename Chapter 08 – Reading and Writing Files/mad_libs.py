#! python3
#
# NAME         : mad_libs.py
#
# DESCRIPTION  : Reads in all text files in the current working directory
#                and lets the user add their own text anywhere the word
#                ADJECTIVE, NOUN, VERB or ADVERB appears in the text file.
#                Writes the result to a new file with prefix 'mad_'.
#
# AUTHOR       : Tim Kornev (@Timmate on GitHub)
#
# CREATED DATE : 4th of July, 2016
#


import os
import re


for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        # Read only files with `.txt` extenstion.
        print()
        print('Reading in {}...'.format(filename))
        read_file = open(filename)
    else:
        # Skip files with other extensions.
        continue

    text = read_file.read()
    read_file.close()

    # Set regular expressions and find matched objects. If no matched objects
    # were found, there is no need to take the user's input and change the
    # original text.
    adj_regex = re.compile(r'ADJECTIVE')
    adj_mo = adj_regex.search(text)
    
    noun_regex = re.compile(r'NOUN')
    noun_mo = noun_regex.search(text)
    
    verb_regex = re.compile(r'\sVERB')  # whitespace is used to ensure
                                        # the keyword VERB was found, not
                                        # the keyword ADVERB.
    verb_mo = verb_regex.search(text)

    adverb_regex = re.compile(r'ADVERB')
    adverb_mo = adverb_regex.search(text)

    if adj_mo or noun_mo or verb_mo or adverb_mo:   # there must be at least one
                                                    # match.
        # Display the original text.                                                    
        print('TEXT: {}'.format(text))
        
        # Take the user's input and modify the text. Ask for the input
        # only if the keyword appears in the text.
        if adj_mo:
            adj = input('Enter an adjective: ')
            text = adj_regex.sub(adj, text)
        if noun_mo:
            noun = input('Enter a noun: ')
            text = noun_regex.sub(noun, text)
        if verb_mo:
            verb = input('Enter a verb: ')
            text = verb_regex.sub(' ' + verb, text)
        if adverb_mo:
            adverb = input('Enter an adverb: ')
            text = adverb_regex.sub(adverb, text)
        
        # Display the modified text.
        print('CHANGED TEXT TO: {}'.format(text))

        # Write the result to a new file.
        print('Writing to mad_{}...'.format(filename))
        write_file = open('mad_{}'.format(filename), 'w')
        write_file.write(text)
        write_file.close()

    else:
        # There are no keywords matches.
        print('Found no keywords.')
