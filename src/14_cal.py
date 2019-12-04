"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

x = input("Enter month and year (MM YYYY): ").split(" ")

# print(x)
# print(*x)

# for n in x:
#   print(n)

# print(len(x))

try: 
  if x == ['']:
    print(calendar.TextCalendar().formatmonth(datetime.now().year, datetime.now().month, w=4, l=2))
  elif len(x) == 1:
    print(calendar.TextCalendar().formatmonth(datetime.now().year, int(x[0]), w=4, l=2))
  elif len(x) == 2:
    print(calendar.TextCalendar().formatmonth(int(x[1]), int(x[0]), w=4, l=2))
except:
  print("Please enter data in MM YYYY format")

