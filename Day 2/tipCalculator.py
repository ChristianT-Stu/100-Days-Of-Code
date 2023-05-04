#Instructions
# Tip Calculator
    #If the bill was $150.00, split between 5 people, with 12% tip.
    #Each person should pay (150.00 / 5) * 1.12 = 33.6
    #Format the result to 2 decimal places = 33.60
    #Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")
tip_perc = input("What percentage tip would you like to give? 10, 12, or 15? ")
person_split = input("How many people to split the bill? ")

converted_bill = float(bill)
converted_tip_perc = float(tip_perc) / 100
converted_person_split = float(person_split)

added_value = (converted_bill / converted_person_split) * converted_tip_perc

split_bill = round(((converted_bill / converted_person_split) + added_value), 2)

print(f'Each person should pay: ${split_bill}')