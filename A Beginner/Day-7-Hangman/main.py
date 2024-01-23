import random
import os
from word_list import word_list
from stages import logo, stages
# from stages import stages

# If you want to clear the console in python, you should use the clear function importining it from os
clear = lambda: os.system('cls')

end_of_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)
# print(f'Hey! This is the solution {chosen_word}')

display = []
for item in chosen_word:
    display += "_"

lives = 6
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f'You\'ve already guessed {guess}')
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose.')
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print('You win.')
    print(stages[lives])

