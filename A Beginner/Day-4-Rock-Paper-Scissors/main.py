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
user = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.')
usuario = int(user)
user_selection = ""
if usuario == 0:
    user_selection = "Rock"
elif usuario == 1:
    user_selection = "Paper"
else:
    user_selection = "Scissors"

pc_selection = ""
azar = random.randint(0,2)
if azar == 0:
    pc_selection = "Rock"
elif azar == 1:
    pc_selection = "Paper"
else:
    pc_selection = "Scissors"

if user_selection == "Rock" and pc_selection == "Rock" or user_selection == "Paper" and pc_selection == "Paper" or user_selection == "Scissors" and pc_selection == "Scissors":
    print(f"You chose\n{user_selection}{choice[usuario]}\nComputer chose\n{pc_selection}{choice[azar]}\nDare")
elif user_selection == "Rock" and pc_selection == "Scissors" or user_selection == "Paper" and pc_selection == "Rock" or user_selection == "Scissors" and pc_selection == "Paper":
    print(f"You chose\n{user_selection}{choice[usuario]}\nComputer chose\n{pc_selection}{choice[azar]}\nYou Win!!!")
else:
    print(f"You chose\n{user_selection}{choice[usuario]}\nComputer chose\n{pc_selection}{choice[azar]}\nWasted...")