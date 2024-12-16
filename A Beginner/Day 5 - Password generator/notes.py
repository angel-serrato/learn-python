# Loops
# For loop
fruits = ['apple', 'orange', 'apple', 'pear', 'banana']
for fruit in fruits:
    print(fruit)
# Sum
students_scores = [634, 912, 385, 148, 932, 500, 759, 877, 415, 703, 309, 286, 157, 914, 93, 787, 25, 42, 910, 592]
total = sum(students_scores)
print(total)
# Max
max = students_scores[0]
for numeros in students_scores:
    if numeros > max:
        max = numeros
print(f"El número mayor es {max}")
# Range
for number in range(1,11):
    print(number)
for number in range(1,101, 5):
    print(number)
# Gaus number 5050
suma = 0
for number in range(1, 101):
    suma = suma + number
print(f"Gauss value {suma}")
# FizzBuzz
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 2 == 0:
        print(number)
    else:
        print(number)