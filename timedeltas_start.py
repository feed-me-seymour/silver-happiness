#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import pandas as pd

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print("today is:" + str(now))

# print today's date one year from now
print("one year from now it will be " + str(now+timedelta(days=365)))

# create a timedelta that uses more than one argument
print("In 2 days and 3 weeks it will be " + str(now+timedelta(days=2, weeks=3)))


# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago, it was " + s)

### How many days until Christmas Day?
today = date.today()
xmasday = date(today.year, 12, 25)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if xmasday < today:
    print("Christmas Day already went by %d days ago" % ((today-xmasday).days))
    xmasday = xmasday.replace(year = today.year+1)
    print(xmasday.ctime())

# Now calculate the amount of time until Christmas Day
time_to_xmasday = xmasday-today
print("It's just", time_to_xmasday.days, "days until Christmas Day")

# seems like pandas (one of the most popular python data libraries) is good for dealing with time, like:

import pandas as pd # normally you'd put this up top
                    # you will need to 'pip install pandas' from a terminal prompt to install the pandas python module
leap_year_day_string = "February 29, 2016"
leap_year_format_string = "%B %d, %Y"

leap_year_datetime = datetime.strptime(leap_year_day_string, leap_year_format_string).date()
print("Leap year: " + leap_year_datetime.strftime('%m/%d/%Y, %H:%M:%S'))

next_year_datetime = leap_year_datetime + pd.DateOffset(years=1)
print("Plus one year: " + next_year_datetime.strftime('%m/%d/%Y, %H:%M:%S'))

today_datetime = datetime.now()
print("Today: " + today_datetime.strftime("%m/%d/%Y, %H:%M:%S"))

plus_one_year_datetime = today_datetime + pd.DateOffset(years=1)
print("Today + One Year: " + plus_one_year_datetime.strftime("%m/%d/%Y, %H:%M:%S"))