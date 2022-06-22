from cards import Card, Rank
from typing import List

def flush(hand:List[Card]) -> bool:
    return len(set([card.suit for card in hand])) == 1

def deuce_flush(hand:List[Card]) -> bool:
    without_deuces = [card for card in hand if card.rank is not Rank.TWO]
    return flush(without_deuces)

def straight(hand:List[Card]) -> bool:
    sorted_hand = sorted(hand, key=lambda card: card.rank.value)
    for i in range(4):
        current_rank = sorted_hand[i].rank.value
        next_rank = sorted_hand[i + 1].rank.value
        if not next_straight(current_rank, next_rank):
            return False
    return True

def next_straight(current_rank, next_rank):
    king_ace = current_rank == 1 and next_rank == 10
    greater_by_one = current_rank + 1 == next_rank
    return king_ace or greater_by_one