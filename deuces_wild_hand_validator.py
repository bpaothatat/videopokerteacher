from turtle import st
from cards import Card, Rank
from collections import Counter
from typing import Dict, List

def four_deuces(hand:List[Card]) -> bool:
    return len([card for card in hand if card.rank == Rank.TWO]) == 4

def royal_flush_with_deuces(hand:List[Card]) -> bool:
    ranks = [card.rank for card in hand]
    return royal_flush(hand) and Rank.TWO in ranks 

def royal_flush_without_deuces(hand:List[Card]) -> bool:
    ranks = [card.rank for card in hand]
    return royal_flush(hand) and Rank.TWO not in ranks 

def royal_flush(hand:List[Card]) -> bool:
    deuces_removed = [card for card in hand if card.rank is not Rank.TWO]
    sorted_hand =  sorted(deuces_removed, key=lambda card: card.rank.value)
    return straight_flush(hand) and sorted_hand[0].rank.value >= Rank.TEN.value

def straight_flush(hand:List[Card]) -> bool:
    return straight(hand) and flush(hand)

def flush(hand:List[Card]) -> bool:
    without_deuces = [card for card in hand if card.rank is not Rank.TWO]
    return len(set([card.suit for card in without_deuces])) == 1

def straight(hand:List[Card]) -> bool:
    result = False
    without_deuces = [card for card in hand if card.rank is not Rank.TWO]
    sorted_hand = sorted(without_deuces, key=lambda card: card.rank.value)
    if len(sorted_hand) > 1:
        lowest = sorted_hand[0].rank.value
        highest = sorted_hand[-1].rank.value
        if highest == 14 and lowest <=5:
            highest = sorted_hand[-2].rank.value
            lowest = 1
        result = highest - lowest <= 4
    else:
        result = True
    return result

def two_pair(hand:List[Card]) -> bool:
    return rank_kind(hand, 2, 2)

def three_of_a_kind(hand:List[Card]) -> bool:
    return rank_kind(hand, 3, None)

def four_of_a_kind(hand:List[Card]) -> bool:
    return rank_kind(hand, 4, None)

def five_of_a_kind(hand:List[Card]) -> bool:
    return rank_kind(hand, 5, None)

def rank_kind(hand:List[Card], first_count:int, second_count:int) -> bool:
    hand_count = rank_count(hand)
    if first_count == second_count:
        counts = Counter(hand_count.values())
        return counts[first_count] == 2
    elif second_count is not None:
        return first_count in hand_count.values() and second_count in hand_count.values()
    else:
        return first_count in hand_count.values()

def rank_count(hand:List[Card]) -> Dict:
    dict = {}
    counts = Counter(card.rank for card in hand)
    twos = sum(map(lambda card : card.rank == Rank.TWO, hand))
    for card in hand:
        if card.rank not in dict.keys():
            if card.rank is not Rank.TWO:
                dict[card.rank] = counts[card.rank] + twos
            else:
                dict[card.rank] = twos
    return dict