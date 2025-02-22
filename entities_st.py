import deck_service_st as service
import deck_reader_st
import random

class Hand():
    def __init__(self):
        self.hand = {}
        self.value = 0

    def draw_2_cards(self, deck):
        self.hand = service.draw_cards(self.hand, 2, deck)
        self.update_value()

    def draw_1_cards(self, deck):
        self.hand = service.draw_cards(self.hand, 1, deck)
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

    def print_cards(self, st):
        x = len(self.hand.keys())
        cards = list(self.hand)
        service.print_x_cards(x, cards, st)
        st.write(f'Сумма очков: {self.value}')

class Dealer(Hand):
    def __init__(self):
        super().__init__()
    
    def print_dealer_cards(self, st):
        cards = list(self.hand)
        service.print_dealer_cards(self, cards, st)
        st.write('Сумма очков: ***')

class Player(Hand):
    def __init__(self):
        super().__init__()
        self.balance = 1000
        self.debt = 0

class Deck():
    def __init__(self):
        self.deck = deck_reader_st.read_deck()
        self.card_costs = deck_reader_st.read_costs(self.deck)
        
    def refresh_current_deck(self):
        self.current_deck = random.sample(self.deck, k = len(self.deck))

    def return_card_cost(self, card):
        self.cost = self.card_costs[card]
        return self.cost