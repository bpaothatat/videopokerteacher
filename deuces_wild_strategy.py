from cards import Card, Rank
from deuces_wild_hand_validator import *

def get_correct_hold_strategy(hand:List[Card]):
    result = [False] * 5
    if two_counter(hand) == 4:
        result = keep_four_deuces(hand)
    return result

def two_counter(hand:List[Card]):
    return len([card for card in hand if card.rank == Rank.TWO])

def keep_four_deuces(hand:List[Card]):
    return [True if card.rank == Rank.TWO else None for card in hand]

def validate_strategy(held:List[bool], expected:List[bool]) -> bool:
    result = True
    for i in range(len(expected)):
        if expected[i] is not None:
            result = result and held[i] == expected[i]
    return result