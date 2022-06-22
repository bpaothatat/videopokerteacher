from cards import Card, Suit, Rank
from deuces_wild_hand_validator import deuce_flush, straight

import unittest

class DeucesWildTest(unittest.TestCase):

    def test_deuces_wild_flush(self):
        #Flush without deuces
        flush_without_deuces_hand = [Card(Suit.CLUB, Rank.ACE), Card(Suit.CLUB, Rank.KING), Card(Suit.CLUB, Rank.QUEEN), Card(Suit.CLUB, Rank.JACK), Card(Suit.CLUB, Rank.TEN)]
        self.assertTrue(deuce_flush(flush_without_deuces_hand))

        #Flush with deuces and different suit
        flush_with_deuces_hand = [Card(Suit.DIAMOND, Rank.TWO), Card(Suit.CLUB, Rank.KING), Card(Suit.CLUB, Rank.QUEEN), Card(Suit.CLUB, Rank.JACK), Card(Suit.CLUB, Rank.TEN)]
        self.assertTrue(deuce_flush(flush_with_deuces_hand))

        #Not a flush
        non_flush_hand = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.KING), Card(Suit.CLUB, Rank.QUEEN), Card(Suit.CLUB, Rank.JACK), Card(Suit.CLUB, Rank.TEN)]
        self.assertFalse(deuce_flush(non_flush_hand))

    def test_straight(self):
        #Royal straight
        royal_straight = [Card(Suit.DIAMOND, Rank.ACE), Card(Suit.CLUB, Rank.KING), Card(Suit.CLUB, Rank.QUEEN), Card(Suit.CLUB, Rank.JACK), Card(Suit.CLUB, Rank.TEN)]
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

if __name__ == '__main__':
    unittest.main()