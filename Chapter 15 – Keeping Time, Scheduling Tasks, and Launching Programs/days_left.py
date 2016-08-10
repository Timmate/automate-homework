#! python3
# 
# NAME         : days_left.py
#
# DESCRIPTION  : Calcululates number of days left until specified dates.
#
# AUTHOR       : Tim Kornev (@Timmate on GitHub)
#
# CREATED DATE : 15th of July, 2016
#


import datetime
from collections import OrderedDict


now = datetime.datetime.now()
year = now.year

# Set dates of holidays, birthdays, anniversaries, etc.
dates = {
    'bill_gates_bday':    {'name': "Bill Gates' birthday",
                           'date': datetime.datetime(year, 10, 28)},
    'halloween':          {'name': 'Halloween',
                           'date': datetime.datetime(year, 10, 31)},
    'saint_patricks_day': {'name': "Saint Patrick's day",
                           'date': datetime.datetime(year, 3, 17)},
    'my_cats_birthday':   {'name': "my cat's birthday",
                           'date': datetime.datetime(year, 6, 30)},
    'new_year':           {'name': "New Year",
                           'date': datetime.datetime(year, 1, 1)},
    'next_study_year':    {'name': "next study year",
                           'date': datetime.datetime(year, 9, 1)}
    }



# Calculate number of days left until each date.
for date in dates:
    dt = dates[date]['date']
    if now > dt:
        # If a date already was this year, use next year.
        next_year = year + 1
        month = dt.month
        day = dt.day
        dt = datetime.datetime(next_year, month, day)

    # Calculate.
    days_left = (dt - now).days

    # Add 'days_left' key and value to each date.
    dates[date]['days_left'] = days_left

print()
# Sort 'dates' dict by days_left in descending order. 
od = OrderedDict(sorted(dates.items(), key=lambda x: x[1]['days_left']))
# Print the result.
for date in od:
    name = od[date]['name']
    days_left = od[date]['days_left']
    print("It's {} day(s) left until {}.".format(days_left, name))
print()
