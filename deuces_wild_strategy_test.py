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

        three_twos_with_nothing = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.SPADE, Rank.TWO), Card(Suit.HEART, Rank.ACE), Card(Suit.DIAMOND, Rank.SEVEN)]
        self.assertTrue(validate_strategy([True, True, True, False, False], get_correct_hold_strategy(three_twos_with_nothing)))

    def test_two_deuces(self):
        two_twos_wild_flush = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.HEART, Rank.TEN), Card(Suit.HEART, Rank.ACE), Card(Suit.HEART, Rank.KING)]
        self.assertTrue(validate_strategy([True, True, True, True, True], get_correct_hold_strategy(two_twos_wild_flush)))
        
        two_twos_five_of_a_kind = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.DIAMOND, Rank.ACE), Card(Suit.HEART, Rank.ACE), Card(Suit.SPADE, Rank.ACE)]
        self.assertTrue(validate_strategy([True, True, True, True, True], get_correct_hold_strategy(two_twos_five_of_a_kind)))

        two_twos_stright_flush = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.DIAMOND, Rank.ACE), Card(Suit.DIAMOND, Rank.THREE), Card(Suit.DIAMOND, Rank.FOUR)]
        self.assertTrue(validate_strategy([True, True, True, True, True], get_correct_hold_strategy(two_twos_stright_flush)))

        two_twos_four_of_a_kind = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.DIAMOND, Rank.FIVE), Card(Suit.HEART, Rank.ACE), Card(Suit.SPADE, Rank.ACE)]
        self.assertTrue(validate_strategy([True, True, False, True, True], get_correct_hold_strategy(two_twos_four_of_a_kind)))

        twos_twos_with_nothing = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.SPADE, Rank.THREE), Card(Suit.HEART, Rank.TEN), Card(Suit.DIAMOND, Rank.SEVEN)]
        self.assertTrue(validate_strategy([True, True, False, False, False], get_correct_hold_strategy(twos_twos_with_nothing)))

    def test_one_deuces(self):
        one_two_wild_flush = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.HEART, Rank.QUEEN), Card(Suit.HEART, Rank.TEN), Card(Suit.HEART, Rank.ACE), Card(Suit.HEART, Rank.KING)]
        self.assertTrue(validate_strategy([True, True, True, True, True], get_correct_hold_strategy(one_two_wild_flush)))
        
        one_two_five_of_a_kind = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.ACE), Card(Suit.DIAMOND, Rank.ACE), Card(Suit.HEART, Rank.ACE), Card(Suit.SPADE, Rank.ACE)]
        self.assertTrue(validate_strategy([True, True, True, True, True], get_correct_hold_strategy(one_two_five_of_a_kind)))

        one_two_stright_flush = [Card(Suit.DIAMOND, Rank.FIVE), Card(Suit.CLUB, Rank.TWO), Card(Suit.DIAMOND, Rank.ACE), Card(Suit.DIAMOND, Rank.THREE), Card(Suit.DIAMOND, Rank.FOUR)]
        self.assertTrue(validate_strategy([True, True, True, True, True], get_correct_hold_strategy(one_two_stright_flush)))

        one_two_four_of_a_kind = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.TWO), Card(Suit.DIAMOND, Rank.FIVE), Card(Suit.HEART, Rank.ACE), Card(Suit.SPADE, Rank.ACE)]
        self.assertTrue(validate_strategy([True, True, False, True, True], get_correct_hold_strategy(one_two_four_of_a_kind)))

        one_two_with_nothing = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.THREE), Card(Suit.SPADE, Rank.SIX), Card(Suit.HEART, Rank.TEN), Card(Suit.DIAMOND, Rank.SEVEN)]
        self.assertTrue(validate_strategy([True, False, False, False, False], get_correct_hold_strategy(one_two_with_nothing)))

    def test_no_deuces(self):
        no_twos_royal_flush = [Card(Suit.HEART, Rank.JACK), Card(Suit.HEART, Rank.QUEEN), Card(Suit.HEART, Rank.TEN), Card(Suit.HEART, Rank.ACE), Card(Suit.HEART, Rank.KING)]
        self.assertTrue(validate_strategy([True, True, True, True, True], get_correct_hold_strategy(no_twos_royal_flush)))
        
        no_two_straight_flush = [Card(Suit.HEART, Rank.SIX), Card(Suit.HEART, Rank.SEVEN), Card(Suit.HEART, Rank.EIGHT), Card(Suit.HEART, Rank.NINE), Card(Suit.HEART, Rank.TEN)]
        self.assertTrue(validate_strategy([True, True, True, True, True], get_correct_hold_strategy(no_two_straight_flush)))

        one_two_with_nothing = [Card(Suit.DIAMOND, Rank.JACK), Card(Suit.CLUB, Rank.THREE), Card(Suit.SPADE, Rank.SIX), Card(Suit.HEART, Rank.TEN), Card(Suit.DIAMOND, Rank.SEVEN)]
        self.assertTrue(validate_strategy([False, False, False, False, False], get_correct_hold_strategy(one_two_with_nothing)))




    def test_discard_all(self):
        four_twos = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.SIX), Card(Suit.SPADE, Rank.FIVE), Card(Suit.HEART, Rank.TEN), Card(Suit.CLUB, Rank.JACK)]
        self.assertTrue(validate_strategy([False, False, False, False, False], get_correct_hold_strategy(four_twos)))

if __name__ == '__main__':
    unittest.main()