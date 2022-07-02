from cards import Card, Rank
from deuces_wild_hand_validator import *

def get_correct_hold_strategy(hand:List[Card]):
    keep_all = [True] * 5
    result = [False] * 5
    twos = number_of_twos(hand)
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
        elif four_to_royal_flush(hand, twos):
            result = keep_four_to_royal_flush(hand, 2)
            ##TODO: Rule 6
        else:
            result = keep_deuces(hand)
    elif twos == 1:
        if  royal_flush(hand) or five_of_a_kind(hand) or straight_flush(hand):
            result = keep_all
        elif four_of_a_kind(hand):
            result = keep_four_of_a_kind(hand)
        elif four_to_royal_flush(hand, twos):
            result = keep_four_to_royal_flush(hand)
        else:
            result = keep_deuces(hand)
    else:
        if royal_flush_without_deuces(hand) or straight_flush(hand):
            result = keep_all
        elif four_to_royal_flush(hand, twos):
            result = keep_four_to_royal_flush(hand)
    return result

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
    card_count = {rank:hand_card_ranks.count(rank) for rank in hand_card_ranks}
    for card_rank, count in card_count.items():
        if count >= 2:
            rank = card_rank
    return [True if card.rank == Rank.TWO or card.rank == rank else False for card in hand]

def four_to_royal_flush(hand:List[Card], two_count:int):
    result = False
    suit = None
    update_hand = hand_without_twos(hand)
    suit_counts = suit_count(update_hand)
    for acutal_suit, count in suit_counts.items():
        if count + two_count is 4:
            suit = acutal_suit
    if suit:
        result = len([card for card in hand if card.rank.value > Rank.NINE.value]) + two_count == 4
    return result

def keep_four_to_royal_flush(hand:List[Card]):
    return [True if card.rank.value > Rank.NINE.value or card.rank is Rank.TWO else False for card in hand]

def validate_strategy(held:List[bool], expected:List[bool]) -> bool:
    result = True
    for i in range(len(expected)):
        if expected[i] is not None:
            result = result and held[i] == expected[i]
    return result