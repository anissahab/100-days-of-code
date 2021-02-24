import random
from decks import card_decks

def deal():
    hand = []
    for i in range(2):
        card = choose_card()
        hand.append(card)
    return hand


def choose_card():
    global card_decks
    card = random.choice(card_decks)
    card_decks.remove(card)
    return card


def check_21(hand):
    total = 0
    for card in hand:
        total += card
    if total > 21:
        if 11 in hand:
            total -= 10
        else:
            return False
    if total <= 21:
        return True

# assigning hands to each player
player_hand = deal()
dealer_hand = deal()
# we can only show one of the dealer's card, let's store it in a separate list
dealer_visible = []
dealer_visible.append(random.choice(dealer_hand))
dealer_visible.append('?')

print(player_hand, dealer_hand)

# lets start the game
print(f'Player cards are {player_hand}.')
print(f"Dealer's cards are {dealer_visible}")

# players turn
while True:
    move = input('Would you like to hit or stand? ').lower()
    if move == 'hit' or move == 'h':
        player_hand.append(choose_card())
        print(player_hand)
        if not check_21(player_hand):
            print('Bust! Looks like the dealer wins this one')
            break
        else:
            continue
