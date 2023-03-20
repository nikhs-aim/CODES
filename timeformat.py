import datetime

# write a function called print_time that takes a time object and print it in the form hour:in:seconds


def print_time(time):
    print(f"{time.hour}:{time.minute}:{time.second}")


# Create a time object representing 9:30:15
time_obj = datetime.time(hour=9, minute=30, second=15)

print_time(time_obj)
