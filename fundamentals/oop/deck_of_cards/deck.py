import card
import player
import random

class Deck(player.Player):
    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards= []

        for s in suits:
            for i in range(2,15):
                str_val = ""
                if i == 14:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append(card.Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def shuffle_deck (self):
        random.shuffle(self.cards)
        return self

    def get_card(self):
        top_card = random.choice(self.cards)
        self.cards.remove(top_card)
        return top_card