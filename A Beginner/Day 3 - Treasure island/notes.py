# If / else statement
age = int(input('How old are you?\n'))
if age >= 18:
    print('You are old enough to vote!')
else:
    print('You are NOT old enough to vote.')
# Modulo operator
# Check odd or even
number = int(input('Type out a number\n '))
if number % 2 == 0:
    print('You are an even number!')
else:
    print('You are an odd number!')
# Nested if else statement
print('Welcome to the rollercoaster!')
height = int(input('How tall are you?\n'))
bill = 0
if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input('How old are you?\n'))
    if age <= 11:
        bill = 5
        print('Child tickets are $5')
    elif age >= 12 and age <= 18:
        bill = 7
        print('Youth tickets are $7')
    elif age >= 45 and age <= 55:
        print('Have free ride on us')
    else:
        bill = 12
        print('Adult tickets are $12')
    photo = input('Do you want to have a photo take')
    if photo == 'yes':
        bill += 3
        print('You are a photo taken!')
    print(f'Your total bill is ${bill}')
else:
    print('Sorry you have to grow taller before you can ride.')
# Python pizza delivery program
print('Welcome to Python Pizza Deliveries!')
size = input('What size pizza do you want? S, M or L: \n')
pepperoni = input('Do you want pepperoni on your pizza? Y or N: \n')
extra_cheese = input('Do you want extra cheese? Y or N: \n')
total_bill = 0
if size == 'S':
    total_bill = 15
elif size == 'M':
    total_bill = 20
elif size == 'L':
    total_bill = 25
else:
    print('Please enter either S, M or L')
if pepperoni == 'Y':
    if size == 'S':
        total_bill += 2
    else:
        total_bill += 3
if extra_cheese == 'Y':
    total_bill += 1
print(f'Your total bill is {total_bill}')
# Logical operators
