from cards import Card, Rank
from deuces_wild_hand_validator import *

def get_correct_hold_strategy(hand:List[Card]):
    keep_all = [True] * 5
    result = [False] * 5
    twos = two_counter(hand)
    if twos == 4:
        result = keep_four_deuces(hand)
    if twos == 3:
        if royal_flush(hand) or five_of_a_kind(hand):
            result = keep_all
        else:
            result = keep_deuces(hand)
    return result

def two_counter(hand:List[Card]):
    return len([card for card in hand if card.rank == Rank.TWO])

def keep_deuces(hand:List[Card]):
    return [True if card.rank == Rank.TWO else None for card in hand]

def keep_four_deuces(hand:List[Card]):
    return [True if card.rank == Rank.TWO else None for card in hand]

def validate_strategy(held:List[bool], expected:List[bool]) -> bool:
    result = True
    for i in range(len(expected)):
        if expected[i] is not None:
            result = result and held[i] == expected[i]
    return result