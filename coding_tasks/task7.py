from datetime import datetime

age_int = int(input("How old are you? "))
name_str = input("What is your name? ")

current_year = datetime.now().year

birth_year = current_year - age_int

print(f"OMG, you are {age_int} years old and you were born in {birth_year}")

# Define the past date - for example, January 1, 2020
# Format: datetime(year, month, day, hour, minute, second)
past_date = datetime(birth_year, 1, 1, 0, 0, 0)

# Get the current date and time
current_date = datetime.now()

# Calculate the difference between the current date and the past date
difference = current_date - past_date

# Calculate the total number of hours
total_hours = difference.total_seconds() / 3600

print(f"You have been alive for around {round(total_hours)} hours.")
