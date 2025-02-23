import deck_reader
import random

class Deck():
    def __init__(self):
        self.deck = deck_reader.read_deck()
        self.card_costs = deck_reader.read_costs(self.deck)
        
    def refresh_current_deck(self):
        self.current_deck = random.sample(self.deck, k = len(self.deck))

    def return_card_cost(self, card):
        self.cost = self.card_costs[card]
        return self.cost