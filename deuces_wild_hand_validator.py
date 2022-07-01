from turtle import st
from cards import Card, Rank
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

def full_house(hand:List[Card]) -> bool:
    return rank_kind(hand, 3, 2)

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
    available_twos = 0
    if Rank.TWO in hand_count:
        available_twos = hand_count.pop(Rank.TWO)
    first, available_twos = check_rank_kind(hand_count, available_twos, first_count)
    second = True
    if second_count:
        second, available_twos = check_rank_kind(hand_count, available_twos, second_count)
    return first and second

def rank_count(hand:List[Card]) -> Dict:
    ranks = [card.rank for card in hand]
    return {rank:ranks.count(rank) for rank in ranks}

def suit_count(hand:List[Card]) -> Dict:
    suits = [card.suit for card in hand]
    return {suit:suits.count(suit) for suit in suits}

def hand_without_twos(hand:List[Card]) -> List[Card]:
    return [card for card in hand if card.rank is not Rank.TWO]

def check_rank_kind(ranks:Dict[Rank, int], available_twos:int, expected_count:int) -> bool:
    result = False
    copy = ranks.copy()
    for rank, count in copy.items():
        if count == expected_count:
            ranks.pop(rank)
            result = True
            break
    
    if not result:
        for rank, count in copy.items():
            if count + available_twos >= expected_count:
                available_twos =  available_twos - (expected_count - count)
                result = True
                ranks.pop(rank)
    return result, available_twos




