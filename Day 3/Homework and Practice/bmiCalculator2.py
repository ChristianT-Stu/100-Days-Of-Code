'''
Instructions
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
'''

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weight_float = float(weight)
height_float = float(height)

bmiCalculatorResult = (round(weight_float / (height_float ** 2)))

if bmiCalculatorResult < 18.5:
    print(f'Your BMI is {bmiCalculatorResult}, you are underweight.')
elif bmiCalculatorResult > 18.5 and bmiCalculatorResult < 25:
    print(f'Your BMI is {bmiCalculatorResult}, you have a normal weight.')
elif bmiCalculatorResult > 25 and bmiCalculatorResult < 30:
    print(f'Your BMI is {bmiCalculatorResult}, you are slightly overweight.')
elif bmiCalculatorResult > 30 and bmiCalculatorResult < 35:
    print(f'Your BMI is {bmiCalculatorResult}, you are obese.')
else:
    print(f'Your BMI is {bmiCalculatorResult}, you are clinically obese.')