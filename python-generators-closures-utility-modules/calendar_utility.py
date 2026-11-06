'''
Calendar utility.
Asks for a year and month, prints that month's calendar, and says whether today's date falls inside it.
'''

import calendar # imports the 'calendar' module to help display the calendar
import datetime # Imports the 'datetime' module to determine today's date.

today = datetime.date.today()
 
# print(dir(calendar)) # allows me to see all the tools in the 'calendar' toolbox

try: 
    print("See a calendar month for a year of choice!")
    year = int(input("Enter the year: "))  # Gets the year from the user and converts the input string into an integer.
    month = int(input("Enter the month (1-12): ")) # Gets the month from the user and converts the input string into an integer.
    print()
    print("===== Calendar =====")
    print(calendar.month(year, month)) # calls the 'month(year, month)' function from the 'calendar' module with 2 separate 
                                    # values/arguments of 'year' and 'month' to import the calendar for the month & year specified.
                                    # IOWs, it calls the month(year, month) function from the calendar module, passing the specified
                                    # year and month as arguments to display the requested calendar.

    if month == today.month and year == today.year:
        # print(f"Today falls inside the month and year entered. Today is {today.month} {today.day}, {today.year}")
        print(f"Today falls inside the month and year entered. Today is {calendar.month_name[today.month]} {today.day}, {today.year}")
    else:
        print("Today's date DOES NOT fall inside the month and year entered!")

except ValueError: # a 'try/catch block' ('try/except block') to ensure the correct data type input is entered, since a 
                    # deliberate 'int()' was done to cast any string input obtained via the 'input()' function.
                    # this covers both issues 1) invalid data 2) "calendar.IllegalMonthError" if some enters value > 12 for 'month'.
                    # "calendar.IllegalMonthError" is a subclass of "ValueError", so it is also caught by your handler when an 
                    # invalid month is supplied. However, calendar.IllegalMonthError is a specific exception raised by the 
                    # calendar module. The existing handler therefore works for both situations.
                    # In other words, it handles invalid input when the user enters something that cannot be converted into an 
                    # integer using int(). Also catches calendar.IllegalMonthError, which is a subclass of ValueError and occurs
                    # when an invalid month is supplied.
    print("Invalid input. Enter the year as a number and the month as a number from 1 to 12!")

print() # space






