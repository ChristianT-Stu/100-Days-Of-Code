#Instructions
# How many total days, weeks, and months wpuld you have left, after selecting your current age, and death age.

age = input("What is your current age? ")
death_age = input("What age will you die at? ")

years_left = int(death_age) - int(age)

years_left_days = years_left * 365
years_left_weeks = years_left * 52
years_left_months = years_left * 12

print(" ")
print(f'You have {years_left_days} days, {years_left_weeks} weeks, and {years_left_months} months left on this Earth.')
print(f'You will live for {years_left} more years. ')