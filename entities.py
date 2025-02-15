import time
import deck_service
import deck_reader
import random

class Hand():
    def __init__(self):
        self.hand = {}
        self.value = 0

    def draw_2_cards(self, deck):
        self.hand = deck_service.draw_cards(self.hand, 2, deck)
        self.update_value()

    def draw_1_cards(self, deck):
        self.hand = deck_service.draw_cards(self.hand, 1, deck)
        self.update_value()

    def update_value(self):
        self.value = 0
        for card in self.hand:
            self.value += self.hand[card]
        if self.value > 21:
            self.check_aces()

    def check_aces(self):
        for card in self.hand:
            if self.hand[card] == 11 and self.value > 21:
                self.hand[card] = 1
                self.value -= 10

    def print_cards(self):
        time.sleep(0.5)
        print(', '.join(self.hand.keys()) + f'. (Сумма очков: {self.value})')

class Dealer(Hand):
    def __init__(self):
        super().__init__()
    
    def print_start_cards(self):
        time.sleep(0.5)
        first_card = list(self.hand)[0]
        print(f'{first_card}, ***' + f'. (Сумма очков: ***)')

class Player(Hand):
    def __init__(self):
        super().__init__()
        self.balance = 1000
        self.debt = 0

class Deck():
    def __init__(self):
        self.deck = deck_reader.read_deck()
        self.card_costs = deck_reader.read_costs(self.deck)
        
    def refresh_current_deck(self):
        self.current_deck = random.sample(self.deck, k = len(self.deck))

    def return_card_cost(self, card):
        self.cost = self.card_costs[card]
        return self.cost