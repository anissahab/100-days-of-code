import random
import time
import sys
from functions import deal, choose_card, check_if_over, check_who_won, hand_sum

# deal cards to each player
player_hand = deal()
dealer_hand = deal()

# a separate list that will only display one of the dealer's cards
dealer_visible = []
# choose a random card from the dealers hand to show
dealer_visible.append(random.choice(dealer_hand))
dealer_visible.append('?')

# to remove
print(player_hand, dealer_hand)

# start game here: show the cards
print(f'Player cards are {player_hand}.')
print(f"Dealer's cards are {dealer_visible}")

# players turn
while True:
    move = input('Would you like to hit or stand? ').lower()
    if move == 'hit' or move == 'h':
        player_hand.append(choose_card())
        print(player_hand)
        if check_if_over(player_hand):
            print('Bust! Looks like the dealer wins this one')
            sys.exit()
            # don't want to show dealers cards
        else:
            continue
    else:
        break

# dealers turn
hit = True
while hit:
    if check_if_over(dealer_hand):
        print('Bust for the dealer! You win this one')
        sys.exit()
    else:
        if hand_sum(dealer_hand) <= 16:
            print(f"The dealer's cards are: {dealer_hand}")
            new_card = choose_card()
            dealer_hand.append(new_card)
            dealer_visible.append(new_card)
            time.sleep(1)
            print('The dealer hits...')
            time.sleep(1)
            print(dealer_hand)
            time.sleep(1)
        else:
            hit = False



# reveal cards and declare winner
time.sleep(2)
print(f"The dealer's hand is {dealer_hand}")
time.sleep(2)
if hand_sum(dealer_hand) == hand_sum(player_hand):
    print('Looks like its a tie!')
    sys.exit()
winner = check_who_won(player_hand, dealer_hand)
if winner == player_hand:
    print(f"Looks like you won! With a hand of {player_hand}")
else:
    print("Looks like the dealer got you! Better luck next time")