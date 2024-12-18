# # Functions with inputs
# def greet(name):
#     print(f"Hello, {name}")
# greet("Jim")
# # Example
# # def funcion(el_parametro)
# #     print(el_parametro)
# #
# # funcion("el_argumento")
# # Life in weeks
# # https://waitbutwhy.com/2014/05/life-weeks.html
# def life_in_weeks(age):
#     weeks = 4680 - (age * 52)
#     print(f"You have {weeks} weeks left.")
# edad = int(input("How old are you?"))
# life_in_weeks(edad)
# # Functions with multiple inputs
# def saludar(name, last_name):
#     print(f"Hello {name}, {last_name}")
# saludar("Angel","Serrato")
# # Using keyword arguments
# saludar(last_name = "Arias", name = "Didier")
# Calculate love score
def calculate_love_score(name1, name2):
    both_names = (name1 + name2).upper()
    contador_true = 0
    contador_love = 0
    for letter in both_names:
        if letter == "T" or letter == "R" or letter == "U" or letter == "E":
            contador_true += 1
        if letter == "L" or letter == "O" or letter == "V" or letter == "E":
            contador_love += 1
    total = str(contador_true) + str(contador_love)
    print(total)

calculate_love_score("Angel", "Gabriela")