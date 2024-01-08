import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
choice = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]
# user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
# user_selection = ""
# if user == 0:
#     user_selection = "Rock"
# elif user == 1:
#     user_selection = "Paper"
# elif user == 2:
#     user_selection = "Scissors"
# else:
#     print('You did not type the number correctly. Try again.')

# pc_selection = ""
# azar = random.randint(0,2)
# if azar == 0:
#     pc_selection = "Rock"
# elif azar == 1:
#     pc_selection = "Paper"
# else:
#     pc_selection = "Scissors"

# if user_selection == "Rock" and pc_selection == "Rock" or user_selection == "Paper" and pc_selection == "Paper" or user_selection == "Scissors" and pc_selection == "Scissors":
#     print(f"You chose\n{user_selection}{choice[user]}\nComputer chose\n{pc_selection}{choice[azar]}\nDraw...")
# elif user_selection == "Rock" and pc_selection == "Scissors" or user_selection == "Paper" and pc_selection == "Rock" or user_selection == "Scissors" and pc_selection == "Paper":
#     print(f"You chose\n{user_selection}{choice[user]}\nComputer chose\n{pc_selection}{choice[azar]}\nYou Win!")
# else:
#     print(f"You chose\n{user_selection}{choice[user]}\nComputer chose\n{pc_selection}{choice[azar]}\nYou lose.")

user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

computer = random.randint(0,2)

if user == computer:
    print(f"You chose\n{user}{choice[user]}\nComputer chose\n{computer}{choice[computer]}\nDraw...")
elif user == 0 and computer == 2 or user == 1 and computer == 0 or user == 2 and computer == 1:
    print(f"You chose\n{user}{choice[user]}\nComputer chose\n{computer}{choice[computer]}\nYou Win!")
elif user < 0 or user > 2:
    print('It isn\'t hard to type a single number.')
    exit()
else:
    print(f"You chose\n{user}{choice[user]}\nComputer chose\n{computer}{choice[computer]}\nYou lose.")