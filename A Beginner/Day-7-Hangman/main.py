import random
# Step 1

word_list = ['angel', 'didier', 'serrato','arias', 'gato', 'perro', 'mono', 'ave', 'gorila']

# Todo 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

# number = random.randint(0, (len(word_list) - 1))
# chosen_word = word_list[number]

# Todo 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()

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
    # display.append("_")
    display += "_"
print(display)

"""
Todo 2 - Loop through each position in the chosen_word; If the letter at that position
matches 'guess' then reveal that letter in the display at that position.
"""

# for letter in chosen_word:
#     if letter == guess:
#         display[]
