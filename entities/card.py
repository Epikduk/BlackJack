class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.value == other.value and self.suit == other.suit
        return False
    
    def __hash__(self):
        return hash((self.value, self.suit))
    
    def __str__(self):
        return f"{self.value} {self.suit}"