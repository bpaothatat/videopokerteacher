from cards import Card, Rank
from typing import List

def flush(hand:List[Card]) -> bool:
    return len(set([card.suit for card in hand])) == 1

def deuce_flush(hand:List[Card]) -> bool:
    without_deuces = [card for card in hand if card.rank is not Rank.TWO]
    return flush(without_deuces)