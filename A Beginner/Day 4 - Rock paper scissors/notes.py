# Randomisation, lists
# Return a random number
import random
import my_module
print(f"This is my favorite number imported from my module {my_module.my_favourite_number}")
random_number = random.randint(1, 10)
print(random_number)
# Random floating numbers
random_another = random.random() * 10
print(random_another)
random_float = random.uniform(0, 100)
print(random_float)
# Random exercise
numero = random.randint(0,1)
if numero == 0:
    print(f"El número es {numero}")
    print("Heads")
else:
    print(f"El número es {numero}")
    print("Tails")
# Lists are data structures, storing single pieces of data
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "California"]
states_of_america.append("Pittsburgh")
for state in states_of_america:
    print(state)
import random
friends = ["Alice", "Bob", "Charlie", "David", "Manuel"]
azar = random.randint(0, len(friends)-1)
azarados = random.choice(friends)
print(friends[azar])
# Nested list
fruits = ["Strawberries", "Apples", "Grapes", "Peaches"]
vegetables = ["Spinach", "Tomatoes", "Potatoes"]
dirty = [fruits, vegetables]
