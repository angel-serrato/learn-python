print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Welcome to the Treasure Island.\nYour mission is to find the treasure.')
camino = input('You are at a cross road. Where do you want to go? Type "left" or "right".\n').lower()
if camino == "left":
    swait = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross.\n').lower()
    if swait == "wait":
        color = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n').lower()
        if color == "red":
            print('You found your ex girlfriend/boyfriend inside that room. Game Over!')
        elif color == "yellow":
            print('YOU WIN!!!')
        elif color == "blue":
            print('You enter a room of beasts. Game Over!')
        else:
            print('Did you type the word correctly?')
    elif swait == "swim":
        print('You do not know how to swim. Game Over!')
    else:
        print('Did you type the word correctly?')
elif camino == "right":
    print('You fell into a hole. Game Over!')
else:
    print('Did you type the word correctly?')