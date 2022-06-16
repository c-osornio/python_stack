from . import deck
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hand= []
    
    def deal(self, my_deck):
        for i in range(26):
            my_cards = deck.Deck.get_card(my_deck)
            self.hand.append(my_cards)
        print(self.hand)