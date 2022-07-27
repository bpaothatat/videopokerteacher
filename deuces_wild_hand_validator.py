from cards import Card, Rank
from typing import Dict, List
from enum import Enum

class Hand(Enum):
    NOTHING = 0
    THREE_OF_A_KIND = 1
    STRAIGHT = 2
    FLUSH = 2
    FULL_HOUSE = 3
    FOUR_OF_A_KIND = 5
    STRIGHT_FLUSH = 9
    FIVE_OF_A_KIND = 15
    WILD_ROYAL_FLUSH = 25
    FOUR_DEUCES = 200
    NATURAL_ROYAL_FLUSH = 800

def hand_evaluator(hand:List[Card]) -> Hand:
    print([card.rank.name + ' of ' + card.suit.name for card in hand])
    hand_value = Hand.NOTHING
    if royal_flush_without_deuces(hand):
        hand_value = Hand.NATURAL_ROYAL_FLUSH
    elif four_deuces(hand):
        hand_value = Hand.FOUR_DEUCES
    elif royal_flush_with_deuces(hand):
        hand_value = Hand.WILD_ROYAL_FLUSH
    elif five_of_a_kind(hand):
        hand_value = Hand.FIVE_OF_A_KIND
    elif straight_flush(hand):
        hand_value = Hand.STRIGHT_FLUSH
    elif four_of_a_kind(hand):
        hand_value = Hand.FOUR_OF_A_KIND
    elif full_house(hand):
        hand_value = Hand.FULL_HOUSE
    elif flush(hand):
        hand_value = Hand.FLUSH
    elif straight(hand):
        hand_value = Hand.STRAIGHT
    elif three_of_a_kind(hand):
        hand_value = Hand.THREE_OF_A_KIND
    return hand_value

def four_deuces(hand:List[Card]) -> bool:
    return number_of_twos(hand) == 4

def royal_flush_with_deuces(hand:List[Card]) -> bool:
    return royal_flush(hand) and Rank.TWO in [card.rank for card in hand] 

def royal_flush_without_deuces(hand:List[Card]) -> bool:
    return royal_flush(hand) and Rank.TWO not in [card.rank for card in hand] 

def royal_flush(hand:List[Card]) -> bool:
    sorted_hand =  sort_by_rank(hand_without_twos(hand))
    return straight_flush(hand) and sorted_hand[0].rank.value >= Rank.TEN.value

def straight_flush(hand:List[Card]) -> bool:
    return straight(hand) and flush(hand)

def flush(hand:List[Card]) -> bool:
    return len(suit_count(hand_without_twos(hand)).keys()) == 1

# TODO: Fix Straight
def straight(hand:List[Card]) -> bool:
    result = True
    sorted_hand = sort_by_rank(hand_without_twos(hand))
    available_twos = number_of_twos(hand)
    for i in range(len(sorted_hand) - 1):
        if sorted_hand[i].rank.value + 1 != sorted_hand[i + 1].rank.value:
            if not (sorted_hand[i + 1].rank.value == 14 and available_twos == 1):
                difference = sorted_hand[i + 1].rank.value - sorted_hand[i].rank.value - 1 
                if available_twos >= difference:
                    available_twos = available_twos - difference
                else: 
                    result = False
                    break
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

def number_of_twos(hand:List[Card]):
    return len([card for card in hand if card.rank == Rank.TWO])

def rank_count(hand:List[Card]) -> Dict:
    ranks = [card.rank for card in hand]
    return {rank:ranks.count(rank) for rank in ranks}

def suit_count(hand:List[Card]) -> Dict:
    suits = [card.suit for card in hand]
    return {suit:suits.count(suit) for suit in suits}

def hand_without_twos(hand:List[Card]) -> List[Card]:
    return [card for card in hand if card.rank is not Rank.TWO]

def sort_by_rank(hand:List[Card]) -> List[Card]:
    return sorted(hand, key=lambda card: card.rank.value)

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




