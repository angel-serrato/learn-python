from art import logo
from data import data
from random import sample

def play():
    should_continue = True
    score = 0
    jugadores = get_two_data()
    player_a = jugadores[0]
    player_b = jugadores[1]
    while should_continue:
        print(logo)
        print(f"Compare A: {player_a['name']}, {player_a['description']}, {player_a['country']}, {player_a['follower_count']}")
        print("VS")
        print(f"Against B: {player_b['name']}, {player_b['description']}, {player_b['country']}, {player_b['follower_count']}")
        user_guess = ""
        while user_guess not in ['a', 'b']:
            try:
                user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
                if user_guess not in ['a', 'b']:
                    print("Invalid input.")
            except ValueError:
                print("Invalid input")
        correct_answer = compare(player_a, player_b)
        if user_guess == correct_answer:
            score += 1
            print(f"You are right! Current score: {score}")
            if correct_answer == "a":
                player_a = player_a
                player_b = get_new_player()
            elif correct_answer == "b":
                player_a = player_b
                player_b = get_new_player()
        elif user_guess != correct_answer:
            print(f"Sorry! That's wrong. Final score: {score}")
            should_continue = False

def compare(player_a, player_b):
    if player_a['follower_count'] > player_b['follower_count']:
        return "a"
    elif player_a['follower_count'] < player_b['follower_count']:
        return "b"

def get_two_data():
    return sample(data, 2)

def get_new_player():
    return sample(data, 1)[0]

play()

# try:
#     age = int(input("How old are you?"))
# except ValueError:
#     print("Type a number.")
#     age = int(input("How old are you?"))