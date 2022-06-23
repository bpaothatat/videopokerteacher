from dataclasses import dataclass
from enum import Enum

class Suit(Enum):
    SPADE = 0
    HEART = 1
    DIAMOND = 2
    CLUB = 3

class Rank(Enum):
    ACE = 14
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

@dataclass(frozen=True)
class Card:
    suit: Suit
    rank: Rank