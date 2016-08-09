#! python3
#
# NAME         : 2048_bot_selenium.py
#
# DESCRIPTION  : Uses `selenium` to play 2048 game online.
#
# AUTHOR       : Tim Kornev (Timmate profile on GitHub)
#
# CREATED DATE : 7th of July, 2016

#
# NOTE: On my Windows 10 OS with Edge browser I could not simulate pressing keys
# with `<elem>.send_keys(<key>)` so I used `ActionChains` to do that. Try
# uncommenting those lines with `ActionChains` if the original method does not work.
#


import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains


# Set constants.
UP = Keys.ARROW_UP
RIGHT = Keys.ARROW_RIGHT
DOWN = Keys.ARROW_DOWN
LEFT = Keys.ARROW_LEFT

URL = 'https://gabrielecirulli.github.io/2048/'

# Open the 2048 game page.
browser = webdriver.Firefox()
browser.get(URL)
time.sleep(5)
html_elem = browser.find_element_by_tag_name('html')
browser.execute_script("window.scrollTo(0, 200)")    # scroll to the screen's center
time.sleep(2)

# Play the game.
times_to_move = 1500   # number of times to move tiles
for i in range(times_to_move):
    for key in (UP, RIGHT, DOWN, LEFT):
        html_elem.send_keys(key)
##        ActionChains(browser).send_keys(key).perform()
##        time.sleep(1)     # uncomment this line to slow down game speed

#
# NOTE: The "all-directions" playing algorithm is quite silly and weak. Feel free
# to modify the code to follow "amlost-always-winning" algorithm that consists of
# having tile with the biggest score in one corner. You can attempt to reach this by
# moving tiles only in two adjacent directions like 'UP-RIGHT', 'UP-LEFT', etc.
# However, sometimes this bot falls into a trap as it cannot continue the game by
# simply moving tiles in the two "main" directions. When it occures, it looks like
# nothing is happening on the game screen at all. To prevent this from happening,
# the bot should sometimes move tiles to other directions. The code below
# represents a simple implementation of this idea:
#
#    for key in (UP, RIGHT):
#        html_elem.send_keys(key)
#        
#        if i % 25 == 0:
#            html_elem.send_keys(DOWN)
#        if i % 150 == 0:
#            html_elem.send_keys(LEFT)
#    
            
    
