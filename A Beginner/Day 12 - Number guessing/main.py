import random
from art import guessing_game

random_number = random.randrange(1, 101)
print(f"The random number is: {random_number}")

def easy(random):
    attempts = 10
    for items in range(attempts):
        print(f"You have {attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if attempts == 0:
            print("You've run out of guesses. Do you want to play again? Type 'y' or 'no'.")
        elif guess > random:
            print("Too high.")
            print("Guess again.")
            attempts = attempts - 1
        elif guess < random:
            print("Too low.")
            print("Guess again.")
            attempts = attempts - 1
        elif guess == random:
            print(f"You got it! The answer is {random}")
            exit()
        else:
            print("I said a number!")
            print("Guess again.")

def hard(random):
    attempts = 5
    for items in range(attempts):
        print(f"You have {attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if attempts == 0:
            print("You've run out of guesses. Do you want to play again? Type 'y' or 'no'.")
        elif guess > random:
            print("Too high.")
            attempts = attempts - 1
        elif guess < random:
            print("Too low.")
            attempts = attempts - 1
        elif guess == random:
            print(f"You got it! The answer is {random}")
            exit()
        else:
            print("I said a number!")
            print("Guess again.")

print(guessing_game)
print("Welcome to the number guessing name!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard':")

if level == "easy":
    easy(random_number)
elif level == "hard":
    hard(random_number)


# print("Too low.")
# print("Too high.")
# print("Guess again.")
# print("You've run out of guesses. Do you want to play again? Type 'y' or 'no'.")
