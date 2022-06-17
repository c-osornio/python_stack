import deck

class Player:
    players = []
    def __init__(self, name):
        self.name = name
        self.hand= []
        self.players.append(self)
    
    def deal(self, my_deck):
        for i in range(26):
            my_cards = deck.Deck.get_card(my_deck)
            self.hand.append(my_cards)
        print(self.hand)

    @classmethod
    def get_players(cls):
        for player in cls.players:
            print(f"Player Name: {player.name}")

    @staticmethod
    def is_valid(name):
        if type(name) == str: 
            x = Player(name)
            print("Valid")
            return x
        else:
            print("Invalid input")
