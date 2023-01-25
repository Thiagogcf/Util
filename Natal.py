import time

# Get the current time
current_time = time.time()

# Set the target time to be the start of the new year
new_year = time.mktime((2024, 1, 1, 0, 0, 0, 0, 0, 0))

# Calculate the number of seconds until the new year
seconds_until_new_year = new_year - current_time

#Calculate the percentage of the year that has passed
current_year = time.gmtime().tm_year
start_of_year = time.mktime((current_year, 1, 1, 0, 0, 0, 0, 0, 0))
percentage = (current_time - start_of_year) / seconds_until_new_year * 100

# Print the result
print(f"There are {seconds_until_new_year} seconds until the new year, {percentage:.2f}% of the year has passed.")
