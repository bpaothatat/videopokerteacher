from cards import Card, Rank
from collections import Counter
from typing import Dict, List

def flush(hand:List[Card]) -> bool:
    return len(set([card.suit for card in hand])) == 1

def deuce_flush(hand:List[Card]) -> bool:
    without_deuces = [card for card in hand if card.rank is not Rank.TWO]
    return flush(without_deuces)

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

def pair(hand:List[Card]) -> bool:
    return rank_kind(hand, 2, None)

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