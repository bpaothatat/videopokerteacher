from cards import Card, Suit, Rank
from deuces_wild_strategy import get_correct_hold_strategy, validate_strategy

import unittest

class DeucesWildTest(unittest.TestCase):
    def test_four_deuces(self):
        four_twos = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.SPADE, Rank.TWO), Card(Suit.HEART, Rank.TWO), Card(Suit.CLUB, Rank.FIVE)]
        self.assertTrue(validate_strategy([True, True, True, True, False], get_correct_hold_strategy(four_twos)))
        self.assertTrue(validate_strategy([True, True, True, True, True], get_correct_hold_strategy(four_twos)))

    def test_three_deuces(self):
        three_twos_wild_flush = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.SPADE, Rank.TWO), Card(Suit.HEART, Rank.ACE), Card(Suit.HEART, Rank.KING)]
        self.assertTrue(validate_strategy([True, True, True, True, True], get_correct_hold_strategy(three_twos_wild_flush)))
        
        three_twos_five_of_a_kind = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.SPADE, Rank.TWO), Card(Suit.HEART, Rank.ACE), Card(Suit.SPADE, Rank.ACE)]
        self.assertTrue(validate_strategy([True, True, True, True, True], get_correct_hold_strategy(three_twos_five_of_a_kind)))

        three_twos_with_nothing = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.SPADE, Rank.TWO), Card(Suit.HEART, Rank.ACE), Card(Suit.SPADE, Rank.TWO)]
        self.assertTrue(validate_strategy([True, True, True, True, True], get_correct_hold_strategy(three_twos_with_nothing)))

    def test_discard_all(self):
        four_twos = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.SIX), Card(Suit.SPADE, Rank.FIVE), Card(Suit.HEART, Rank.TEN), Card(Suit.CLUB, Rank.JACK)]
        self.assertTrue(validate_strategy([False, False, False, False, False], get_correct_hold_strategy(four_twos)))

if __name__ == '__main__':
    unittest.main()