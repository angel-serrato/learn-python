print('Welcome to the tip calculator.')
bill = input('What was the total bill? $')
tip = input('What percentage would you like to give? 10, 12, or 15? ')
people = int(input('How many people to split the bill? '))
# total_bill = round((((float(bill) * int(tip)) / 100) + float(bill)) / people, 2)
# we can add the two decimal places by using format
total_bill = "{:.2f}".format((((float(bill) * int(tip)) / 100) + float(bill)) / people, 2)
print(f'Each person should pay: ${total_bill}')