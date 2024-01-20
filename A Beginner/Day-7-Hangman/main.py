import random
# Step 1

word_list = ['angel', 'didier', 'serrato','arias', 'gato', 'perro', 'mono', 'ave', 'gorila']

# Todo 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

number = random.randint(0, (len(word_list) - 1))
chosen_word = word_list[number]

# Todo 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()

# Todo 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
        
for letter in chosen_word:
    if letter == guess:
        print('right')
    else:
        print('wrong')