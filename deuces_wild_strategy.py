from cards import Card, Suit, Rank
from deuces_wild_hand_validator import *

def get_correct_hold_strategy(hand:List[Card]):
    keep_all = [True] * 5
    result = [False] * 5
    twos = two_counter(hand)
    if twos == 4:
        result = keep_four_deuces(hand)
    elif twos == 3:
        if royal_flush(hand) or five_of_a_kind(hand):
            result = keep_all
        else:
            result = keep_deuces(hand)
    elif twos == 2:
        if royal_flush(hand) or five_of_a_kind(hand) or straight_flush(hand):
            result = keep_all
        elif four_of_a_kind(hand):
            result = keep_four_of_a_kind(hand)
        else:
            result = keep_deuces(hand)
    return result

def two_counter(hand:List[Card]):
    return len([card for card in hand if card.rank == Rank.TWO])

def keep_deuces(hand:List[Card]):
    return [True if card.rank == Rank.TWO else None for card in hand]

def keep_four_deuces(hand:List[Card]):
    return [True if card.rank == Rank.TWO else None for card in hand]

def keep_four_of_a_kind(hand:List[Card]):
    """
    Used only for hands with 2 or less threes
    """
    rank = None
    hand_card_ranks = [card.rank for card in hand if card.rank is not Rank.TWO]
    print(hand_card_ranks)
    card_count = {rank:hand_card_ranks.count(rank) for rank in hand_card_ranks}
    for card_rank, count in card_count.items():
        if count >= 2:
            rank = card_rank
    return [True if card.rank == Rank.TWO or card.rank == rank else False for card in hand]



def validate_strategy(held:List[bool], expected:List[bool]) -> bool:
    result = True
    for i in range(len(expected)):
        if expected[i] is not None:
            result = result and held[i] == expected[i]
    return result