import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
letras = int(input("How many letters would you like in your password?\n"))
simbolos = int(input("How many symbols would you like in your password?\n"))
numeros = int(input("How many numbers would you like in your password?\n"))
password = ""
for lacosa in range(0, letras):
    password += random.choice(letters)
for lacosa in range(0, numeros):
    password += random.choice(numbers)
for lacosa in range(0, simbolos):
    password += random.choice(symbols)
list_password = list(password)
random.shuffle(list_password)
shuffled_password = "".join(list_password)
print(f"La contraseña inicial es {password} y mezclada es {shuffled_password}")


