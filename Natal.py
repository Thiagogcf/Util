from datetime import datetime, timedelta

# Get the current date and time
now = datetime.now()

# Christmas is on December 25th, so we need to find the date of the next December 25th
if now.month == 12 and now.day == 25:
    # If it's already Christmas, the next one is next year
    next_christmas = datetime(now.year + 1, 12, 25)
else:
    # Otherwise, the next Christmas is this year
    next_christmas = datetime(now.year, 12, 25)

# Calculate the difference between the current date and the next Christmas
difference = next_christmas - now

# Print the number of days until Christmas
print(f"There are {difference.days} days until Christmas!")
