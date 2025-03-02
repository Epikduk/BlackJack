import random
from entities.card import Card

class Deck():
    CARD_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    CARD_SUITS = ['крести', 'буби', 'черви', 'пики']
    CARD_COSTS_MAP = {
        '2': 2,
        '3': 3,
        '4': 4, 
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11
    }
    
    def __init__(self):
        self.deck = Deck.__create_deck__()
        self.current_deck = []
        
    def __create_deck__():
        deck = []
        for suit in Deck.CARD_SUITS:
            for value in Deck.CARD_VALUES:
                card = Card(value, suit)
                deck.append(card)
        return deck
        
    def refresh_current_deck(self):
        self.current_deck = random.sample(self.deck, k = len(self.deck))

    def return_card_cost(self, card: Card):
        return Deck.CARD_COSTS_MAP[card.value]