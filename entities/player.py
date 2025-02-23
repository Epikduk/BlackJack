from entities.hand import Hand

class Player(Hand):
    def __init__(self):
        super().__init__()
        self.balance = 1000
        self.debt = 0