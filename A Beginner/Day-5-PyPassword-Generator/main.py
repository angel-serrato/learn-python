import random
from random import sample

"""
Method 1
"""
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print('Welcome to the PyPassword Generator!')
# letras = int(input('How many letters would you like in your password?\n'))
# simbolos = int(input('How many symbols would you like?\n'))
# numeros = int(input('How many numbers would you like?\n'))
# password = ""
# for item in range(0, letras):
#     password += random.choice(letters)
# for item2 in range(0, simbolos):
#     password += random.choice(symbols)
# for item2 in range(0, numeros):
#     password += random.choice(numbers)
# print(f'Here is your password: {password}')

"""
Method 2
"""
# def password_generator(longitud):

#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#     # sequence = letters + numbers + symbols
#     contrasena = sample(letters, longitud)
#     resultado = "".join(contrasena)
#     return resultado

# number = int(input('How many?'))
# generated = password_generator(number)
# print(f"Here is your password {generated}")

"""
Method 3
"""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')
letras = int(input('How many letters would you like in your password?\n'))
numeros = int(input('How many numbers would you like?\n'))
simbolos = int(input('How many symbols would you like?\n'))
password = ""
for item in range(0, letras):
    password += random.choice(letters)
for item2 in range(0, numeros):
    password += random.choice(numbers)
for item2 in range(0, simbolos):
    password += random.choice(symbols)
# The sample method returns a list with a randomly selection of a specified number of items from a squence
random_string = random.sample(password, len(password))
pwd = "".join(random_string)
print(f'Here is your password: {pwd}')
