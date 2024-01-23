import random
# Step 1

word_list = ['angel', 'didier', 'serrato','arias', 'gato', 'perro', 'mono', 'ave', 'gorila']

# Todo 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

# number = random.randint(0, (len(word_list) - 1))
# chosen_word = word_list[number]

# Todo 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# guess = input("Guess a letter: ").lower()

# Todo 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
        
# for letter in chosen_word:
#     if letter == guess:
#         print('right')
#     else:
#         print('wrong')

# Step 2
        
# Todo 1 - Create an empty list called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was 'apple', display should be ["_","_","_","_","_"].
        
print(f'This is the solution {chosen_word}')
display = []
for item in chosen_word:
    display += "_"
print(display)

# Method two
# for letter in range(len(chosen_word)):
#     display += "_"

"""
Todo 2 - Loop through each position in the chosen_word; If the letter at that position
matches 'guess' then reveal that letter in the display at that position.
"""
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print('You win.')
"""
Todo 3 - Print display and you should see the guessed letter in the correct position and
every other letter replace with "_".
"""

# Step 3

# Todo 1 - Use a while loop to let the user guess again. The loop should only stop once
# the user has guessed all the letters in the chosen_word and display has no more
# blanks.

