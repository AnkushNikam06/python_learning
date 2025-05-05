# Q: Display the current date and time and create a code for it.

import datetime

now = datetime.datetime.now()

print("Current date and time: ")

print(now.strftime("%Y-%m-%d %H:%M:%S.%f"))

# The above code will display the current date and time in the format year-month-day hour:minute:seconds whenever it is run.
