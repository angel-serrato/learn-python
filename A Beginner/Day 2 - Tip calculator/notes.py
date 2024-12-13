# Primitive data types
print("Hello"[0])
print("Hello"[-1])
print(123_456_789)
print(3.141516)
#
len('hello')
print(type('abc'))
print(type(123))
print(type(3.14))
print(type(True))
#
print(int(123) + int(456))
#
print('Number of letters in your name: ' + str(len(input('Enter your name: \n'))))
# PEMDAS Left to Right
# Parentheses Exponents Multiplication/Division Addition/Substraction
print(3 * (3 + 3) / 3 - 3)
#
bmi = 84 / 1.65 ** 2
print(round(bmi, 2))
# F-strings
print(f'hola {bmi}')