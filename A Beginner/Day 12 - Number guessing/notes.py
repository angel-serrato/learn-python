# Local and Global scope
enemies = 1

def increase_enemies():
    # The global statement
    global enemies
    enemies += 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function {enemies}")

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# There is no block scope in python
# Global constants
# Cuando estan en mayuscula recuerdas que son constantes con scope global y que no le debes cambiar su valor
PI = 3.1415
GOOGLE_URL = "https://www.google.com"


