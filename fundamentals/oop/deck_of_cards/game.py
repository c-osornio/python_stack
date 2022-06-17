import deck
import player
import war

# Deck is created, shows cards and shuffles
bicycle = deck.Deck()
# bicycle.show_cards()
bicycle.shuffle_deck()
# player 1 and 2 are created with empty hands
player1 = player.Player.is_valid("Charlie")
player2 = player.Player.is_valid("Aidee")
# both players are delt half of the deck each
player1.deal(bicycle)
player2.deal(bicycle)
# Players battle it out. Each players shows their top card and the player showing
# the higher point_val wins the battle. Players battle until all cards are used.
# Player with the most won battles wins the war! *Aces point_value = 14. 
war.playWar(player1, player2)
# Deck is shuffled for a new game
bicycle.shuffle_deck()