import random

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
jugador = []
crupier = []
puntuacion_jugador = 0
puntuacion_crupier = 0

still_playing = True

while still_playing:
    def deal_card():
        jugador.append(random.choice(card))
        jugador.append(random.choice(card))
        crupier.append(random.choice(card))
        crupier.append(random.choice(card))
        print(jugador)

        print(f"Your cards: [{jugador[0]}] and [{jugador[1]}]")
        print(f"Computer's first card: [{crupier[0]}] and [hidden card]")
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        print("Your final hand: ")
        print("Computer's final hand: ")

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'no': ").lower()
    if play == 'y':
        deal_card()
    else:
        still_playing = False
        print("Thank you for playing!")
        exit()

