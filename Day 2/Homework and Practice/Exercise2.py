# Instructions
#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# 🚨 Don't change the code below 👇
weight = input("enter your weight in kg: ")
height = input("enter your height in m: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weight_float = float(weight)
height_float = float(height)

bmiCalculatorResult = (weight_float / (height_float ** 2))

print(int(bmiCalculatorResult))