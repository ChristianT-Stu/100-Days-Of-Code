import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. ")

choice_num = int(choice)

rock_num = 0
paper_num = 1
scissors_num = 2

if choice_num == rock_num:
    print(rock)
elif choice_num == paper_num:
    print(paper)
elif choice_num == scissors_num:
    print(scissors)

print("Computer Chose:")

computer_choice = random.randint(0,2)

if computer_choice == rock_num:
    print(rock)
elif computer_choice == paper_num:
    print(paper)
elif computer_choice == scissors_num:
    print(scissors)

if choice_num == 0 and computer_choice == 1:
    print("You lose")
elif choice_num == 0 and computer_choice == 2:
    print("You win")
elif choice_num == 0 and computer_choice == 0:
    print("It's a tie")
elif choice_num == 1 and computer_choice == 2:
    print("You lose")
elif choice_num == 1 and computer_choice == 0:
    print("You win")
elif choice_num == 1 and computer_choice == 1:
    print("It's a tie")
elif choice_num == 2 and computer_choice == 0:
    print("You lose")
elif choice_num == 2 and computer_choice == 1:
    print("You win")
elif choice_num == 2 and computer_choice == 2:
    print("It's a tie")


