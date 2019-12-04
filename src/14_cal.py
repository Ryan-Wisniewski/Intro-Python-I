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

# c = calendar.TextCalendar()
# s = c.formatmonth(1994,9)
# print(s)

# c = calendar.Calendar(firstweekday=0)
# for s in c.itermonthdays(1,1):  
#   print(s)

# x = input("Enter comma-separated year then month: ").split(',')
# print('list',x)

def get_calendar():
  # print('arg',arg)
  c = calendar.TextCalendar()
  t = datetime.today()
  s = c.formatmonth(t.year, t.month)
  if len(sys.argv) < 2:
    return s
  elif len(sys.argv) == 2:
    s = c.formatmonth(t.year, int(sys.argv[1]))
    return s
  elif len(sys.argv) == 3:
    s = c.formatmonth(int(sys.argv[2]), int(sys.argv[1]))
    return s
    
print(get_calendar())