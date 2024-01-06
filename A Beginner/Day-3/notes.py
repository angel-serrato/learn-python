"""
if / else statement
if condition:
    do this
else:
    do this
"""
"""
Comparison operators
>
<
>=
<=
== equal to
!= not equal to
"""
"""
modulo in python
"""
number = int(input('Give me a number...'))
if number % 2 ==  0:
    print('This is an even number')
else:
    print('This is an odd number')
"""
Example
"""
print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm? '))
bill = 0
if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input('What is your age? '))
    if age < 12:
        print('Child tickets are $5.')
        bill = 5
    elif age <= 18:
        print('Youth tickets are $7.')
        bill = 7
    else:
        print('Adult tickets are $12.')
        bill = 12
    photo = input('Do you want a photo? Yes or No?')
    if photo == "y":
        print('The fee is $3')
        bill = bill + 3
    print(f'The final bill is {bill}')
else:
    print('Sorry, you have to grow taller before you can ride.')
"""
leap year / año bisiesto
"""
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print('Leap year')
    else:
      print('Not leap year')
  else: 
    print('Leap year')
else:
  print('Not leap year')
"""
pizza order practice
"""
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
bill = 0
if size == "S":
  bill += 15
  if add_pepperoni == "Y":
    bill += 2
  if extra_cheese == "":
    bill += 1
if size == "M":
  bill += 20
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1
if size == "L":
  bill += 25
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1
print(f'Your final bill is: ${bill}.')
"""
logical operators
"""
