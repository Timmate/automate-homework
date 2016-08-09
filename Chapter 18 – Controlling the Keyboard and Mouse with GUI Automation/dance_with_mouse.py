#! python3
#
# NAME         : dance_with_mouse.py
#
# DESCRIPTION  : Memorizes mouse moves pattern or repeats an existing one.
#
# AUTHOR       : Tim Kornev (Timmate profile on GitHub)
#
# CREATED DATE : 23rd of July, 2016
#


import os
import sys
import time

import pyautogui

# If changing this filename, modify code that import module in 'MEMORIZE' part.
FILENAME = 'file_with_mouse_moves.py'


print()
choice = None
while choice not in ('MEMORIZE', 'REPEAT'):
    choice = input('Enter MEMORIZE or REPEAT: ')

if choice == 'MEMORIZE':
    # Record all moves and write results to a file.

    moves = []   # store all recorded moves here

    print()
    print('Press ENTER to start recording. ')
    print('Press Ctrl-C to end recording. ')
    input()     # press ENTER to start

    # Give the user some time to prepare.
    for sec in range(5, 0, -1):
        print('{} sec(s)...'.format(str(sec)))
        time.sleep(1)

    # Start recording.
    print('REC.')
    try:
        start_position = pyautogui.position()
        moves.append(start_position)
        while True:
            position = pyautogui.position()
            if position == moves[-1]:   # the cursor is not moving
                continue
            else:
                moves.append(position)

    except KeyboardInterrupt:     # if Ctrl-C hotkey combination was pressed
        print()
        print('STOP.')
        print('Writing results to {}...'.format(FILENAME))
        write_file = open(FILENAME, 'w')
        write_string = 'pattern = ' + str(moves)
        write_file.write(write_string)
        write_file.close()
        print('Done.')
        print()

else:
    # Load pattern from the file and repeat all moves.
    try:
        from file_with_mouse_moves import pattern
    except ImportError:
        print('Oops! Found no file. :(')
        sys.exit()

    print()
    print('Press ENTER to start repeating. ')
    print('Press Ctrl-C to end repeating. ')
    input()     # press ENTER to start

    # Give the user some time to prepare.
    for sec in range(5, 0, -1):
        print('{} sec(s)...'.format(str(sec)))
        time.sleep(1)
    print('REP.')

    # Repeat all moves.
    try:
        for coordinates in pattern:
            x, y = coordinates
            pyautogui.moveTo(x, y)

        #
        # NOTE: With the code below the cursor moves faster. Uncomment
        # this block of code and comment the upper block to try it.
        #
##
##        for each_third in range(0, len(pattern) - 1, 3):
##            coordinates = pattern[each_third]
##            x, y = coordinates
##            pyautogui.moveTo(x, y)
        print()
        print('Done.')
        print()

    except KeyboardInterrupt:    # handle Ctrl-C exception.
        print('STOP.')
        print()
        print('Done')
        print()
