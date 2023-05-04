#Instructions
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

"""
It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

"""

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = 90 - int(age)

years_left_days = years_left * 365
years_left_weeks = years_left * 52
years_left_months = years_left * 12

print(f'You have {years_left_days} days, {years_left_weeks} weeks, and {years_left_months} months left.')

#current_age = int(age)

#current_age_days = current_age * 365
#current_age_years = current_age * 52
#current_age_months = current_age * 12