from cards import Card, Suit, Rank
from random import randrange
from typing import List
from enum import Enum

class Deck:
    def __init__(self) -> None:
        self.deck = [Card(suit, rank) for suit in Suit for rank in Rank]
        self.dealt = []

    def __str__(self) -> str:
        return str(self.deck)

    def __len__(self) -> int:
        return len(self.deck)

    def deal_hand(self) -> list:  
        return [self.deal_card() for i in range(5)]

    def redeal_hand(self, hand:List[Card], kept:List[bool]):
        for i in range(5):
            if not kept[i]:
                hand[i] = self.deal_card()
        return hand

    def deal_card(self) -> Card:
        card = self.deck[randrange(52)]
        while card in self.dealt:
            card = self.deck[randrange(52)]
        self.dealt.append(card)
        return card

    def reset(self) -> None:
        self.dealt = []

class HandState(Enum):
    NEW_HAND = 0
    DEALT = 1