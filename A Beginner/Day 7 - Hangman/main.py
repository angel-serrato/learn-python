import random
import hangman_words
import hangman_art

def play_hangman():
    chosen_word = random.choice(hangman_words.words)

    placeholder = ""
    for n in range(len(chosen_word)):
        placeholder = placeholder + "_"
    list_guess = list(placeholder)

    print(f"Welcome to the Hangman game!")
    print(hangman_art.hangman_logo)
    print("##################################")
    print(f"The word you need to guess has {len(chosen_word)} letters.")
    print(f"Let's begin! Here's the word: {" ".join(list_guess)}")
    # print(f"Just for testing purposes: {chosen_word}.")
    print("##################################")

    lifes = 6
    while lifes > 0:
        guess = input("\nGuess a letter (or press '0' to quit):\n  ").lower()
        if guess == '0':
            print(f"Game over! Thanks for playing.")
            break
        if len(guess) != 1 or not guess.isalpha():
            print("Error! Please enter only one letter.")
            continue
        if guess in chosen_word:
            print(f"Good job! The letter {guess} is in the word.")
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    list_guess[i] = guess
            print(f"Current word: {list_guess}")
        else:
            lifes -= 1
            print(f"Incorrect! The letter {guess} is not in the word.")
            print(f"You have {lifes} guess(es) left.")
            print(f"Current word: {list_guess}")
        if "".join(list_guess) == chosen_word:
            print(f"Congratulations! You've guessed the word: {chosen_word}")
            break
        print(hangman_art.hangman_stages[6 - lifes])

    if lifes == 0:
        print(f"\nOh no! You've run out of guesses. The word was: {chosen_word}.")
        print("Thanks for playing! Try again!")

while True:
    play_hangman()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break