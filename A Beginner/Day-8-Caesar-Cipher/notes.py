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