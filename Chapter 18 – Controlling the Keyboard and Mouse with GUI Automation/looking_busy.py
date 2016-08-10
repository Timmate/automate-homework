#! python3
#
# NAME         : looking_busy.py
#
# DESCRIPTION  : Simulates a dumb human that moves the mouse.
#
# AUTHOR       : Tim Kornev (@Timmate on GitHub)
#
# CREATED DATE : 9th of August, 2016
#


import time

import pyautogui


print()
print('Press Ctrl-C to exit.')

try:
    while True:
        pyautogui.moveRel(1, 1)
        for i in range(10):
            time.sleep(1)
            
except KeyboardInterrupt:
    print()
    print('Done.')
    print()
