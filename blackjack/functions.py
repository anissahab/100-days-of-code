from decks import card_decks
import random

# makes a list of 2 cards
def deal():
    hand = []
    for i in range(2):
        card = choose_card()
        hand.append(card)
    return hand

# picks a random card from the deck and removes it from the list
def choose_card():
    global card_decks
    card = random.choice(card_decks)
    card_decks.remove(card)
    return card


def check_if_over(hand):
    total = sum(hand)
    if total > 21:
        if 11 in hand:
            total -= 10
        else:
            return True
    if total <= 21:
        return False

def hand_sum(hand):
    total = sum(hand)
    if total > 21:
        if 11 in hand:
            total -= 10
    return total

# if no busts happen
def check_who_won(hand1, hand2):
    if hand_sum(hand1) > hand_sum(hand2):
        return hand1
    else:
        return hand2

