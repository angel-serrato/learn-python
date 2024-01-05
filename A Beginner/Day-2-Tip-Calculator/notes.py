# Data types, variables, strings.
"""
Data Types => String
"""
# this is called subscripting => pulling out a particular element of the string
print('Hello'[4]) # it returns the first character of the string
"""
Integer
"""
print("123" + "345")
print(123 + 345)
# to visualize numbers more easily we add _ 
print(123_456_798)
"""
Float or floating point number
"""
3.14159
"""
Boolean
"""
True
False
"""
type function checking
"""
num_char = len(input("What is your name?\n"))
print(type(num_char))
"""
str function convertion
"""
new_num_char = str(num_char)
print('Your name has ' + new_num_char + ' characters.')
"""
Mathematical operators
"""
3 + 5
7 - 4
3 * 5
# when you are dividing you will end up with a floating number
40 / 5
2 ** 3
# PEMDAS This calculation goes from left to right
# Parentheses
# Exponents
# Multiplication
# Division
# Addition
# Substraction
"""
round function
"""
print(round(8/3)) # 2
print(round(8/3, 2)) # 2 is the given decimals
"""
floor division
"""
print(round(8//3)) # 2
result = 4 / 2
result /= 2
print(result) # result = 1
score = 1
score += 1 # score = score + 1
# += -= *= /=
"""
f strings
"""
puntaje = 10
altura = 1.8
gana = True
print('your score is ' + str(puntaje))
print(f"Your score is {puntaje}, your heigth is {altura}, you are winning is {gana}")