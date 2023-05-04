#Instructions
# How many total days, weeks, and months would you have been alive if you made it to 90 years old.

age = input("What is your current age? ")
death_age = input("What age will you die at? ")

current_age = int(age)

current_age_days = current_age * 365
current_age_years = current_age * 52
current_age_months = current_age * 12

years_left = int(death_age) - int(age)

years_left_days = years_left * 365
years_left_weeks = years_left * 52
years_left_months = years_left * 12

total_time_alive = current_age + years_left

total_time_alive_days = total_time_alive * 365
total_time_alive_weeks = total_time_alive * 52
total_time_alive_months = total_time_alive * 12

print(f'You lived {total_time_alive_days} days, {total_time_alive_weeks} weeks, and {total_time_alive_months} months on this Earth.')