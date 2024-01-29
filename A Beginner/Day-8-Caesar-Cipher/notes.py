"""
Simple function
Create a function called greet().
Write 3 print statements inside the function.
Call the greet function and run your code.
"""

def greet():
    print("Hi Angel")

greet()

"""
Function that allows for input
"""

def greating(name):
    print(f"Hola {name}")

greating("Angela")

"""
Function with more than one input
We have to be aware of the position parameter
"""

def greating(name, lastname):
    print(f"Hola {name} {lastname}")

greating("Angela","Serrato")

"""
Moving around the parameters
"""

def calculate(a, b, c):
    print(a)
    print(b)
    print(c)

calculate(c=1, b=2, a=3)

"""
Cans of paint exercise
"""

# Write your code below this line 👇
import math
def paint_calc(height, width, cover):
  cans = math.ceil((height * width) / cover)
  print(f'You\'ll need {cans} cans of paint.')
# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.
# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

"""
Prime number
"""

# Write your code below this line 👇
def prime_checker(number):
  for n in range(2, number):
    if number % n == 0:
      print('It\'s not a prime number.')
      return False
  print('It\'s a prime number.')
  return True
# Write your code above this line 👆
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)