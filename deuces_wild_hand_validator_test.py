from cards import Card, Suit, Rank
from deuces_wild_hand_validator import *

import unittest

class DeucesWildTest(unittest.TestCase):

    def test_deuces_wild_flush(self):
        #Flush without deuces
        flush_without_deuces_hand = [Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.KING), Card(Suit.CLUB, Rank.QUEEN), Card(Suit.CLUB, Rank.JACK), Card(Suit.CLUB, Rank.TEN)]
        self.assertTrue(flush(flush_without_deuces_hand))

        #Flush with deuces and different suit
        flush_with_deuces_hand = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.KING), Card(Suit.CLUB, Rank.QUEEN), Card(Suit.CLUB, Rank.JACK), Card(Suit.CLUB, Rank.TEN)]
        self.assertTrue(flush(flush_with_deuces_hand))

        #Not a flush
        non_flush_hand = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.KING), Card(Suit.CLUB, Rank.QUEEN), Card(Suit.CLUB, Rank.JACK), Card(Suit.CLUB, Rank.TEN)]
        self.assertFalse(flush(non_flush_hand))

    def test_straight(self):
        #Royal straight with deuces
        royal_straight = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.KING), Card(Suit.CLUB, Rank.TWO), Card(Suit.CLUB, Rank.JACK), Card(Suit.CLUB, Rank.TEN)]
        self.assertTrue(straight(royal_straight))

        #Random middle straight
        random_middle_straight = [Card(Suit.DIAMOND, Rank.SIX), Card(Suit.CLUB, Rank.SEVEN), Card(Suit.CLUB, Rank.EIGHT), Card(Suit.CLUB, Rank.NINE), Card(Suit.CLUB, Rank.TEN)]
        self.assertTrue(straight(random_middle_straight))

        #Lower straight
        lower_straight =  [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.TWO), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.FOUR), Card(Suit.CLUB, Rank.FIVE)]
        self.assertTrue(straight(lower_straight))

        #Non stright
        non_straight = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.TWO), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.SIX), Card(Suit.CLUB, Rank.FIVE)]
        self.assertFalse(straight(non_straight))

    def test_full_house(self):
        #Full house with twos
        full_house_with_twos = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.TWO), Card(Suit.CLUB, Rank.THREE), Card(Suit.SPADE, Rank.THREE), Card(Suit.DIAMOND, Rank.THREE)]
        self.assertTrue(full_house(full_house_with_twos))

        #Full house without twos
        full_house_without_twos = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.THREE), Card(Suit.SPADE, Rank.THREE), Card(Suit.DIAMOND, Rank.THREE)]
        self.assertTrue(full_house(full_house_without_twos))

        #Not full house
        non_straight = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.TWO), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.SIX), Card(Suit.CLUB, Rank.FIVE)]
        self.assertFalse(full_house(non_straight))

    def test_two_pair(self):
        #Two pair with twos
        two_pair_with_twos = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.TWO), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.FIVE)]
        self.assertTrue(two_pair(two_pair_with_twos))

        #Two pair with no twos
        two_pair_with_no_twos = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.FIVE)]
        self.assertTrue(two_pair(two_pair_with_no_twos))

        #Single pair
        single_pair = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.TWO), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.SIX), Card(Suit.CLUB, Rank.FIVE)]
        self.assertFalse(two_pair(single_pair))

        #None matching
        none_matching = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.FOUR), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.SIX), Card(Suit.CLUB, Rank.FIVE)]
        self.assertFalse(two_pair(none_matching))
        
    def test_three_of_a_kind(self):
        #Three of a kind with twos
        three_of_a_kind_with_twos = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.TWO), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.FIVE)]
        self.assertTrue(three_of_a_kind(three_of_a_kind_with_twos))

        #Three of a kind with no twos
        three_of_a_kind_with_no_twos = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.FIVE)]
        self.assertTrue(three_of_a_kind(three_of_a_kind_with_no_twos))

        #None matching
        non_pair = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.FOUR), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.SIX), Card(Suit.CLUB, Rank.FIVE)]
        self.assertFalse(three_of_a_kind(non_pair))

    def test_four_of_a_kind(self):
        #Four of a kind with twos
        four_of_a_kind_with_twos = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.TWO), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.TWO), Card(Suit.CLUB, Rank.FIVE)]
        self.assertTrue(four_of_a_kind(four_of_a_kind_with_twos))

        #Four of a kind with no twos
        four_of_a_kind_with_no_twos = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.FIVE)]
        self.assertTrue(four_of_a_kind(four_of_a_kind_with_no_twos))

        #None matching
        non_pair = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.FOUR), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.SIX), Card(Suit.CLUB, Rank.FIVE)]
        self.assertFalse(four_of_a_kind(non_pair))

    def test_five_of_a_kind(self):
        #Five of a kind with twos
        five_of_a_kind_with_twos = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.TWO), Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.TWO), Card(Suit.CLUB, Rank.ACE)]
        self.assertTrue(five_of_a_kind(five_of_a_kind_with_twos))

        #None matching
        non_pair = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.FOUR), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.SIX), Card(Suit.CLUB, Rank.FIVE)]
        self.assertFalse(five_of_a_kind(non_pair))

    def test_four_deuces(self):
        #Four twos
        four_twos = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.TWO), Card(Suit.SPADE, Rank.TWO), Card(Suit.HEART, Rank.TWO), Card(Suit.CLUB, Rank.FIVE)]
        self.assertTrue(four_deuces(four_twos))

        #Three twos
        three_twos = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.TWO), Card(Suit.SPADE, Rank.TWO), Card(Suit.HEART, Rank.TWO), Card(Suit.CLUB, Rank.FIVE)]
        self.assertFalse(four_deuces(three_twos))

        #No two
        no_twos= [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.FOUR), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.SIX), Card(Suit.CLUB, Rank.FIVE)]
        self.assertFalse(four_deuces(no_twos))

    def test_royal_flush_with_deuces(self):
        #Royal straight with deuces
        royal_straight_with_deuces = [Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.KING), Card(Suit.CLUB, Rank.TWO), Card(Suit.CLUB, Rank.JACK), Card(Suit.CLUB, Rank.TEN)]
        self.assertTrue(royal_flush_with_deuces(royal_straight_with_deuces))

        #Royal straight with out deuces
        royal_straight_without_deuces = [Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.KING), Card(Suit.CLUB, Rank.QUEEN), Card(Suit.CLUB, Rank.JACK), Card(Suit.CLUB, Rank.TEN)]
        self.assertFalse(royal_flush_with_deuces(royal_straight_without_deuces))
        
        #Not royal flush
        not_royal_flush= [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.FOUR), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.SIX), Card(Suit.CLUB, Rank.FIVE)]
        self.assertFalse(royal_flush_with_deuces(not_royal_flush))

    def test_royal_flush_without_deuces(self):
        #Royal straight with deuces
        royal_straight_with_deuces = [Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.KING), Card(Suit.CLUB, Rank.TWO), Card(Suit.CLUB, Rank.JACK), Card(Suit.CLUB, Rank.TEN)]
        self.assertFalse(royal_flush_without_deuces(royal_straight_with_deuces))

        #Royal straight with out deuces
        royal_straight_without_deuces = [Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.KING), Card(Suit.CLUB, Rank.QUEEN), Card(Suit.CLUB, Rank.JACK), Card(Suit.CLUB, Rank.TEN)]
        self.assertTrue(royal_flush_without_deuces(royal_straight_without_deuces))
        
        #Not royal flush
        not_royal_flush= [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.FOUR), Card(Suit.CLUB, Rank.THREE), Card(Suit.CLUB, Rank.SIX), Card(Suit.CLUB, Rank.FIVE)]
        self.assertFalse(royal_flush_without_deuces(not_royal_flush))

if __name__ == '__main__':
    unittest.main()