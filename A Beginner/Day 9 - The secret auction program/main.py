from my_dict import diccionario
print("Welcome to the secret auction program.")

def mayor(lacosa):
    lamasalta = 0
    ganador = ""
    for bidder in lacosa:
        elmonto = lacosa[bidder]
        print(elmonto)
        if elmonto > lamasalta:
            lamasalta = elmonto
            ganador = bidder
    # persona_oferta = max(diccionario, key=diccionario.get)
    # mayor_oferta = diccionario.get(persona_oferta)
    print(f"The winner is {ganador} with ${lamasalta} money")

should_continue = True

while should_continue:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    diccionario[name] = bid
    should_continue = input("Is there any other bid? Type 'yes' or 'no'.\n").lower()
    if should_continue == 'yes':
        print("\n" * 10)
    else:
        mayor(diccionario)
        should_continue = False
        print("Thank you for bidding!")

with open("my_dict.py", "w") as file:
    file.write(f"diccionario = {diccionario}")

with open("my_dict.py", "w") as file:
    file.write("diccionario = {}")