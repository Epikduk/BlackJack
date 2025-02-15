import time
import deck_service

class Hand():
    def __init__(self):
        self.hand = {}
        self.value = 0

    def draw_2_cards(self):
        self.hand = deck_service.draw_cards(self.hand, 2)
        self.update_value()

    def draw_1_cards(self):
        self.hand = deck_service.draw_cards(self.hand, 1)
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