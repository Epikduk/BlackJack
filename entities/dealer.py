import time
from entities.hand import Hand

class Dealer(Hand):
    def __init__(self):
        super().__init__()
    
    def print_start_cards(self):
        time.sleep(0.5)
        first_card = list(self.hand)[0]
        print(f'{first_card}, ***' + f'. (Сумма очков: ***)')