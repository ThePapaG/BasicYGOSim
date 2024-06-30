#!/usr/bin/python

class Card:

    __name: str
    __details: dict
    __tags: list[str] | None

    def __init__(self, card_name: str, card_details: dict):
        self.__name = card_name
        self.__details = card_details
        self.__tags = card_details.get('tags')

    @property
    def name(self) -> str:
        """The name of the card"""
        return self.__name
    
    @property
    def name_lower(self) -> str:
        """The name of the card in lower case"""
        return self.name.lower()
    
    @property
    def tags(self) -> list[str] | None:
        """The cards tags"""
        return self.__tags
    
    @property
    def details(self) -> dict | None:
        """The details used to describe the card"""
        return self.__details
    
    @property
    def card_free_count(self) -> int:
        """How many free cards this card counts as"""
        if self.name_lower == "upstart goblin":
            return 1
        if self.name_lower == "pot of prosperity" or self.name_lower == "pot of extravagance":
            return 6
        if self.name_lower == "pot of duality":
            return 3
        if self.name_lower == "pot of desires":
            return 2
        else:
            return 0

    @property 
    def card_is_free(self) -> bool:
        """If this card is considered a free card"""
        return self.card_free_count > 0