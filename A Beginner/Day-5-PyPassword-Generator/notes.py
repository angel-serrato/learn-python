"""
loops
for loop
"""
# items = ['angel', 'didier', 'serrato', 'arias']
# for name in items:
#     print(name)
"""
for loop exercise
"""
# Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# Write your code below this row 👇
# mayor = student_scores[0]
# for item in student_scores:
#   if item > mayor:
#     mayor = item
# print(f"The highest score in the class is: {mayor}")
"""
for loops with a range function
the last digit inside the range is not included in the loop
for number in range(a, b):
   print(number)
"""
# suma = 0
# for number in range(0, 101):
#    suma += number
#    print(suma)
# the number 3 represents the step inside the range
# suma = 0
# for number in range(0, 101, 3):
#    suma += number
#    print(suma)
"""
example
"""
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️
# Write your code here 👇
suma = 0
for item in range(1, target + 1):
  if item % 2 == 0:
    suma += item
print(suma)
"""
FizzBuzz example
"""
# Write your code here 👇
for number in range(1,101):
  if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
  elif number % 3 == 0:
    print('Fizz')
  elif number % 5 == 0:
    print('Buzz')
  else:
    print(number)