from utils.player import Deck
from utils.player import Player

class Board:
    def __init__(self, turn_count, active_cards, history_cards):

        self.turn_count = turn_count
        self.active_cards = active_cards
        self.history_cards = history_cards

    def start_game(self):
        deck = Deck
        deck.fill_deck()
        list_distributed = deck.distribute(self, players)
        while len(list_distributed)<=52:
            for player_name in self.players:
                self.turn_count += 1
                for i in range(len(list_distributed)
                    for player_cards in list_distributed:
                        player = Player()
                        player.play()
                        active_cards = player_cards.pop(i)















