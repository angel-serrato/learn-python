print("Welcome to the tip calculator!")
bill = float(input('What was the total bill?\n'))
tip = float(input('How much tip would you like to give? 10 12 15 ?\n'))
people = int(input('How many people to split the bill?\n'))
percentage = (bill * tip) / 100
total = bill + percentage
person = round(total / people, 2)
print(f'Each person should pay: ${person}')