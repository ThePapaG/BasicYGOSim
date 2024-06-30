#!/usr/bin/python

import random
from Card import Card

class Deck:

    __cards: list[Card]

    def __init__(self, cards: list[Card]):
        missing_count = 40 - len(cards)
        if (missing_count > 0):
            cards.extend([Card("Empty Card", {"tags": ["Empty", "Blank", "Non Engine"]})] * missing_count)
        self.__cards = cards

    def __draw_card(self) -> Card:
        """Draw a card from the deck"""
        card = random.choice(self.deck_list)
        self.__cards.remove(card)
        return card

    def draw(self, count: int) -> list[Card]:
        """Draw a hand from the deck"""
        hand = list()

        for i in range(count):
            card = self.__draw_card()
            if (card.card_is_free):
                hand.extend(self.draw(card.card_free_count))
            else:
                hand.append(card)
        
        return hand

    @property
    def deck_list(self) -> list[Card]:
        """The deck list"""
        return self.__cards
    
    @property
    def deck_count(self) -> int:
        """The count of the deck"""
        return len(self.__cards)
    
def BuildDeck(input: dict) -> Deck:
    """Build a deck from a dictionary"""
    deck_list = input['deck']

    cards = list()
    for card, details in deck_list.items():
        qty = 1 if details.get('qty') is None else details.get('qty')
        cards.extend([Card(card, details)] * qty)

    return Deck(cards)