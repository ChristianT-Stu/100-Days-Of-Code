#Instructions
#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

num1 = two_digit_number[0]
num2 = two_digit_number[1]

two_digit_sum = int(num1) + int(num2)

print(two_digit_sum)