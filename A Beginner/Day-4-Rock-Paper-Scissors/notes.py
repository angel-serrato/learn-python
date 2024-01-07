"""
Random module
Python uses mersenne twister
"""
import random
import module
number = random.randint(1,100)
print(number)
print(module.pi)
"""
random floating number
"""
random_float = random.random()
print(random_float)
# Random numbers not including the number 5
decimales = random.random() * 5
print(decimales)
"""
Python lists
A list is a data structure, a way of storing data
fruits = [item1, item2]
They are inside square brackets []
"""
states_us = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia']
print(states_us[1]) # pennsylvania
print(states_us[-1]) # It starts counting from the end of the list in this case Georgia
states_us[0] = 'Angel' # It changes the item in the 0 index position
# Add an item at the end of the list
states_us.append('Angelaland')
# Add two more items to the end of the list
# states_us.extend('Serrato', 'Arias')
"""
Banker roulette exercise
"""
# names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
# import random
# azar = random.randint(0, (len(names) - 1))
# print(f"{names[azar]} is going to buy the meal today!")
"""
Nested lists
"""
fruits = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
vegetables = ['camila', 'pedro', 'carlos']
dirty = [fruits, vegetables]
print(dirty)
"""
Treasure map
"""
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
temp = position[0].upper()
columna = 0
if temp == "A":
  columna = 1
elif temp == "B":
  columna = 2
else:
  columna = 3
fila = int(position[1])
map[fila - 1][columna - 1] = 'X'
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
