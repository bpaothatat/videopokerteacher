from cards import Card, Suit, Rank
from deuces_wild_hand_validator import *
from deuces_wild_strategy import *

import unittest

class DeucesWildTest(unittest.TestCase):
    def test_four_deuces(self):
        four_deuces_test = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.SPADE, Rank.TWO), Card(Suit.HEART, Rank.TWO), Card(Suit.CLUB, Rank.FIVE)]
        self.assertTrue(validate_strategy([True, True, True, True, False], get_correct_hold_strategy(four_deuces_test)))
        self.assertTrue(validate_strategy([True, True, True, True, True], get_correct_hold_strategy(four_deuces_test)))

    def test_three_deuces(self):
        wild_flush_test = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.SPADE, Rank.TWO), Card(Suit.HEART, Rank.ACE), Card(Suit.HEART, Rank.KING)]
        self.assertEqual([True, True, True, True, True], get_correct_hold_strategy(wild_flush_test))
        
        five_of_a_kind_test = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.SPADE, Rank.TWO), Card(Suit.HEART, Rank.ACE), Card(Suit.SPADE, Rank.ACE)]
        self.assertEqual([True, True, True, True, True], get_correct_hold_strategy(five_of_a_kind_test))

        three_twos_test = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.SPADE, Rank.TWO), Card(Suit.HEART, Rank.ACE), Card(Suit.DIAMOND, Rank.SEVEN)]
        self.assertEqual([True, True, True, False, False], get_correct_hold_strategy(three_twos_test))

    def test_two_deuces(self):
        wild_flush_test = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.HEART, Rank.TEN), Card(Suit.HEART, Rank.ACE), Card(Suit.HEART, Rank.KING)]
        self.assertEqual([True, True, True, True, True], get_correct_hold_strategy(wild_flush_test))
        
        five_of_a_kind_test = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.DIAMOND, Rank.ACE), Card(Suit.HEART, Rank.ACE), Card(Suit.SPADE, Rank.ACE)]
        self.assertEqual([True, True, True, True, True], get_correct_hold_strategy(five_of_a_kind_test))

        stright_flush_test = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.DIAMOND, Rank.ACE), Card(Suit.DIAMOND, Rank.THREE), Card(Suit.DIAMOND, Rank.FOUR)]
        self.assertEqual([True, True, True, True, True], get_correct_hold_strategy(stright_flush_test))

        four_of_a_kind_test = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.DIAMOND, Rank.FIVE), Card(Suit.HEART, Rank.ACE), Card(Suit.SPADE, Rank.ACE)]
        self.assertEqual([True, True, False, True, True], get_correct_hold_strategy(four_of_a_kind_test))

        near_to_royal_flush = [Card(Suit.HEART, Rank.SIX), Card(Suit.HEART, Rank.TWO), Card(Suit.DIAMOND, Rank.TWO), Card(Suit.HEART, Rank.JACK), Card(Suit.HEART, Rank.TEN)]
        self.assertEqual([False, True, True, True, True], get_correct_hold_strategy(near_to_royal_flush))
        
        twos_twos= [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.SPADE, Rank.THREE), Card(Suit.HEART, Rank.TEN), Card(Suit.DIAMOND, Rank.SEVEN)]
        self.assertEqual([True, True, False, False, False], get_correct_hold_strategy(twos_twos))

    def test_one_deuces(self):
        wild_flush_test = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.HEART, Rank.QUEEN), Card(Suit.HEART, Rank.TEN), Card(Suit.HEART, Rank.ACE), Card(Suit.HEART, Rank.KING)]
        self.assertEqual([True, True, True, True, True], get_correct_hold_strategy(wild_flush_test))
        
        five_of_a_kind_test = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.ACE), Card(Suit.DIAMOND, Rank.ACE), Card(Suit.HEART, Rank.ACE), Card(Suit.SPADE, Rank.ACE)]
        self.assertEqual([True, True, True, True, True], get_correct_hold_strategy(five_of_a_kind_test))

        stright_flush_test = [Card(Suit.DIAMOND, Rank.FIVE), Card(Suit.CLUB, Rank.TWO), Card(Suit.DIAMOND, Rank.ACE), Card(Suit.DIAMOND, Rank.THREE), Card(Suit.DIAMOND, Rank.FOUR)]
        self.assertEqual([True, True, True, True, True], get_correct_hold_strategy(stright_flush_test))

        four_of_a_kind_test = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.TWO), Card(Suit.DIAMOND, Rank.FIVE), Card(Suit.HEART, Rank.ACE), Card(Suit.SPADE, Rank.ACE)]
        self.assertEqual([True, True, False, True, True], get_correct_hold_strategy(four_of_a_kind_test))

        near_to_royal_flush = [Card(Suit.HEART, Rank.SIX), Card(Suit.HEART, Rank.TWO), Card(Suit.HEART, Rank.QUEEN), Card(Suit.HEART, Rank.JACK), Card(Suit.HEART, Rank.TEN)]
        self.assertEqual([False, True, True, True, True], get_correct_hold_strategy(near_to_royal_flush))

        full_house_test = [Card(Suit.HEART, Rank.TWO), Card(Suit.DIAMOND, Rank.ACE), Card(Suit.SPADE, Rank.THREE), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.THREE)]
        self.assertEqual([True, True, True, True, True], get_correct_hold_strategy(full_house_test))

        three_of_a_kind_test = [Card(Suit.HEART, Rank.ACE), Card(Suit.DIAMOND, Rank.ACE), Card(Suit.SPADE, Rank.FIVE), Card(Suit.CLUB, Rank.TWO), Card(Suit.CLUB, Rank.THREE)]
        self.assertEqual([True, True, False, True, False], get_correct_hold_strategy(three_of_a_kind_test))

        straight_test = [Card(Suit.SPADE, Rank.TWO), Card(Suit.DIAMOND, Rank.SIX), Card(Suit.SPADE, Rank.FIVE), Card(Suit.CLUB, Rank.FOUR), Card(Suit.CLUB, Rank.THREE)]
        self.assertEqual([True, True, True, True, True], get_correct_hold_strategy(straight_test))

        flush_test = [Card(Suit.HEART, Rank.TEN), Card(Suit.HEART, Rank.SIX), Card(Suit.HEART, Rank.JACK), Card(Suit.HEART, Rank.FOUR), Card(Suit.SPADE, Rank.TWO)]
        self.assertEqual([True, True, True, True, True], get_correct_hold_strategy(flush_test))

        one_two = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.THREE), Card(Suit.SPADE, Rank.SIX), Card(Suit.HEART, Rank.TEN), Card(Suit.DIAMOND, Rank.SEVEN)]
        self.assertEqual([True, False, False, False, False], get_correct_hold_strategy(one_two))

    def test_no_deuces(self):
        royal_flush_test = [Card(Suit.HEART, Rank.JACK), Card(Suit.HEART, Rank.QUEEN), Card(Suit.HEART, Rank.TEN), Card(Suit.HEART, Rank.ACE), Card(Suit.HEART, Rank.KING)]
        self.assertEqual([True, True, True, True, True], get_correct_hold_strategy(royal_flush_test))
        
        near_to_royal_flush = [Card(Suit.HEART, Rank.SIX), Card(Suit.HEART, Rank.KING), Card(Suit.HEART, Rank.QUEEN), Card(Suit.HEART, Rank.JACK), Card(Suit.HEART, Rank.TEN)]
        self.assertEqual([False, True, True, True, True], get_correct_hold_strategy(near_to_royal_flush))

        straight_flush_test = [Card(Suit.HEART, Rank.SIX), Card(Suit.HEART, Rank.SEVEN), Card(Suit.HEART, Rank.EIGHT), Card(Suit.HEART, Rank.NINE), Card(Suit.HEART, Rank.TEN)]
        self.assertEqual([True, True, True, True, True], get_correct_hold_strategy(straight_flush_test))

        four_of_a_kind_test = [Card(Suit.HEART, Rank.ACE), Card(Suit.DIAMOND, Rank.ACE), Card(Suit.SPADE, Rank.ACE), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.THREE)]
        self.assertEqual([True, True, True, True, False], get_correct_hold_strategy(four_of_a_kind_test))

        full_house_test = [Card(Suit.HEART, Rank.ACE), Card(Suit.DIAMOND, Rank.ACE), Card(Suit.SPADE, Rank.THREE), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.THREE)]
        self.assertEqual([True, True, True, True, True], get_correct_hold_strategy(full_house_test))

        three_of_a_kind_test = [Card(Suit.HEART, Rank.ACE), Card(Suit.DIAMOND, Rank.ACE), Card(Suit.SPADE, Rank.FIVE), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.THREE)]
        self.assertEqual([True, True, False, True, False], get_correct_hold_strategy(three_of_a_kind_test))

        straight_test = [Card(Suit.HEART, Rank.SEVEN), Card(Suit.DIAMOND, Rank.SIX), Card(Suit.SPADE, Rank.FIVE), Card(Suit.CLUB, Rank.FOUR), Card(Suit.CLUB, Rank.THREE)]
        self.assertEqual([True, True, True, True, True], get_correct_hold_strategy(straight_test))

        flush_test = [Card(Suit.HEART, Rank.TEN), Card(Suit.HEART, Rank.SIX), Card(Suit.HEART, Rank.JACK), Card(Suit.HEART, Rank.FOUR), Card(Suit.HEART, Rank.THREE)]
        self.assertEqual([True, True, True, True, True], get_correct_hold_strategy(flush_test))

        nothing_test = [Card(Suit.DIAMOND, Rank.JACK), Card(Suit.CLUB, Rank.THREE), Card(Suit.SPADE, Rank.SIX), Card(Suit.HEART, Rank.TEN), Card(Suit.DIAMOND, Rank.SEVEN)]
        self.assertEqual([False, False, False, False, False], get_correct_hold_strategy(nothing_test))

    def test_discard_all(self):
        nothing = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.SIX), Card(Suit.SPADE, Rank.FIVE), Card(Suit.HEART, Rank.TEN), Card(Suit.CLUB, Rank.JACK)]
        self.assertEqual([False, False, False, False, False], get_correct_hold_strategy(nothing))

if __name__ == '__main__':
    unittest.main()