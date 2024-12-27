# How to debug
# 1 - Describe the problem
# 2 - Reproduce the bug
# 3 - Play computer
# 4 - Fix the errors
# Try and except block

try:
    age = int(input("How old are you?"))
except ValueError:
    print("Type a number.")
    age = int(input("How old are you?"))

if age > 18:
    print("You can buy candies.")

# 5 - Print is your friend
# 6 - Use a debugger

import random
# Module was created inside the folder
import maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,4,5])

# 7 - Take a break
# 8 - Ask a friend
# 9 - Run often
# 10 - Ask Stackoverflow

