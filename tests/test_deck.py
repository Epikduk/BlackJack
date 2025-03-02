import entities
import unittest

class DeckTestCase(unittest.TestCase):
    def test_deck_init(self):
        deck = entities.Deck()
        self.assertEqual(len(deck.deck), 52)
        for value in entities.Deck.CARD_VALUES:
            cards_with_value = [card for card in deck.deck if card.value == value]
            self.assertEqual(len(cards_with_value), 4)

if __name__ == '__main__':
    unittest.main()