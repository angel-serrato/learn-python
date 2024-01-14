"""
Functions
len() range() print()
def => defining a function
"""
def my_function():
    print('Hello from a function')

my_function()
"""
Arguments or parameters
Remember to execute the function or call the function
"""
def greeting(f_name, l_name):
    print(f'Hello {f_name} {l_name}')

greeting('Angel', 'Serrato')

"""
Indentation
"""
sky = 'clear'
def other_function():
    if sky == 'clear':
        print('blue')
    elif sky == 'cloudy':
        print('grey')
    print('hello')
print('world')
"""
https://reeborg.ca/index_en.html
While loop
while something_is_true:
    # do something
"""
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# number = 6
# while number > 0:
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#     number -= 1
#     print(number)
"""
Another example
"""
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# jump()
# while not at_goal():
#     jump()

# while at_goal() != True:
#     jump()
"""
Another exercise
"""
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     if wall_in_front() == True:
#         jump()
#     else:
#         move()
"""
Another exercise
"""
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     while wall_on_right() == True:
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear() == True:
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front() == True:
#         jump()
#     elif wall_in_front() == False:
#         move()

