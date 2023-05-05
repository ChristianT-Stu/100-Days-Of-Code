"""
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15

Medium Pizza: $20

Large Pizza: $25

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1
"""

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

size_s = 15
size_m = 20
size_l = 25

pep_s = 2
pep_m_l = 3

ext_c = 1

if size == "S":
    if add_pepperoni == "Y" and extra_cheese == "Y":
            print(f"Your final bill is: ${size_s + pep_s + ext_c}.")
    elif add_pepperoni == "N" and extra_cheese == "Y":
            print(f"Your final bill is: ${size_s + ext_c}.")
    elif add_pepperoni == "Y" and extra_cheese == "N":
            print(f"Your final bill is: ${size_s + pep_s}.")
    elif add_pepperoni == "N" and extra_cheese == "N":
            print(f"Your final bill is: ${size_s}.")

if size == "M":
    if add_pepperoni == "Y" and extra_cheese == "Y":
            print(f"Your final bill is: ${size_m + pep_m_l + ext_c}.")
    elif add_pepperoni == "N" and extra_cheese == "Y":
            print(f"Your final bill is: ${size_m + ext_c}.")
    elif add_pepperoni == "Y" and extra_cheese == "N":
            print(f"Your final bill is: ${size_m + pep_m_l}.")
    elif add_pepperoni == "N" and extra_cheese == "N":
            print(f"Your final bill is: ${size_m}.")
if size == "L":
    if add_pepperoni == "Y" and extra_cheese == "Y":
            print(f"Your final bill is: ${size_l + pep_m_l + ext_c}.")
    elif add_pepperoni == "N" and extra_cheese == "Y":
            print(f"Your final bill is: ${size_l + ext_c}.")
    elif add_pepperoni == "Y" and extra_cheese == "N":
            print(f"Your final bill is: ${size_l + pep_m_l}.")
    elif add_pepperoni == "N" and extra_cheese == "N":
            print(f"Your final bill is: ${size_l}.")