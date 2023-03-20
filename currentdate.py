# use the datetime module and write a program that gets the current date and prints the day of the week

import datetime

# Get the current date
current_date = datetime.date.today()

# Print the day of the week
print(current_date.strftime("%A"))
