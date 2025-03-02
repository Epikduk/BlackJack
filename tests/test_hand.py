import entities
import unittest

class HandTestCase(unittest.TestCase):
    def test_check_aces(self):
        card1 = entities.Card('9', 'буби')
        card2 = entities.Card('A', 'буби')
        card3 = entities.Card('A', 'крести')
        hand = entities.Hand()
        hand.hand[card1] = 9
        hand.update_value()
        self.assertEqual(hand.value, 9)
        hand.hand[card2] = 11
        hand.update_value()
        self.assertEqual(hand.value, 20)
        hand.hand[card3] = 11
        hand.update_value()
        self.assertEqual(hand.value, 21)

if __name__ == '__main__':
    unittest.main()