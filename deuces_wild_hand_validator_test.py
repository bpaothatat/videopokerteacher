from cards import Card, Suit, Rank
from deuces_wild_hand_validator import deuce_flush

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

if __name__ == '__main__':
    unittest.main()