import random
from art import logo


def display_hands(player_hand, computer_hand, player_total):
    """Display the hands of both players"""
    print(f"\nYour cards: {player_hand}, current score: {player_total}")
    print(f"Computer's first card: {computer_hand[0]}")


def display_final_hand(player_hand, computer_hand, player_total, computer_total, message):
    """Display the final hand of both players"""
    print(f"\n-----------------{message}-----------------")
    print(f"Your final hand: {player_hand}, final score: {player_total}")
    print(f"Computer's final hands: {computer_hand}, final score: {computer_total}\n")


def calculate_cards(hand):
    """Gets the sum of the hand"""
    total_score = sum(hand)
    if total_score > 21:
        # Check if player has 11
        if 11 in hand:
            idx = hand.index(11)
            hand[idx] = 1
            total_score -= 10
    return total_score


def play_blackjack():
    """Starts a game of Blackjack"""
    computer_cards = []
    player_cards = random.choices(cards, k = 2)
    computer_cards.append(random.choice(cards))
    user_score = calculate_cards(player_cards)
    computer_score = calculate_cards(computer_cards)
    display_hands(player_cards, computer_cards, user_score)
    if user_score == 21:
        user_score = 0  # Blackjack
        display_final_hand(player_cards, computer_cards, user_score, computer_score,
                           "You have a Blackjack! You Win!")
        return

    add_card = True
    while add_card:
        get_another_card = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
        if get_another_card == "y":
            player_cards.append(random.choice(cards))
            user_score = calculate_cards(player_cards)
            display_hands(player_cards, computer_cards, user_score)
            if user_score > 21:
                display_final_hand(player_cards, computer_cards, user_score, computer_score,
                                   "You went over. You Lose!")
                return
        elif get_another_card == "n":
            add_card = False

    # Computers' second card
    computer_cards.append(random.choice(cards))
    computer_score = calculate_cards(computer_cards)
    if computer_score == 21:
        computer_score = 0 # Blackjack
        display_final_hand(player_cards, computer_cards, user_score, computer_score,
                           "Computer has Blackjack! You Lose!")
        return
    elif user_score == 21:
        user_score = 0  # Blackjack
        display_final_hand(player_cards, computer_cards, user_score, computer_score,
                           "You have a Blackjack! You Win!")
        return
    elif computer_score < 17:
        while computer_score < 17:
            computer_cards.append(random.choice(cards))
            computer_score = calculate_cards(computer_cards)
            if computer_score > 21:
                display_final_hand(player_cards, computer_cards, user_score, computer_score,
                                   "Computer went over! You Win!")
                return
            elif computer_score == 21:
                computer_score = 0  # Blackjack
                display_final_hand(player_cards, computer_cards, user_score, computer_score,
                                   "Computer has Blackjack! You Lose!")
                return

    if user_score > computer_score:
        display_final_hand(player_cards, computer_cards, user_score, computer_score,
                           "Your hand is bigger! You Win!")
    elif user_score < computer_score:
        display_final_hand(player_cards, computer_cards, user_score, computer_score,
                           "Computer's hand is bigger! You Lose!")
    elif user_score == computer_score:
        display_final_hand(player_cards, computer_cards, user_score, computer_score,
                           "Draw!")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

continue_playing = True

while continue_playing:
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game == 'y':
        print("\n" * 20)
        print(logo)
        play_blackjack()
    else:
        print("\nOkay. Have a nice day!")
        continue_playing = False
