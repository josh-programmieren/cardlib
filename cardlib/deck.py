from cardlib.card import Card
import random # for shuffling
import json # for saving and loading decks
import os # for saving and loading decks
class Deck:
    """This class represents a deck of cards"""
    def __init__(self,cards:list[Card]) -> None:
        """Initialize a deck of cards"""
        self.cards = cards
        self.shuffle()
    def shuffle(self) -> None:
        """Shuffle the deck"""
        random.shuffle(self.cards)
    def __str__(self) -> str:
        """Return a string representation of the deck"""
        cards=""
        for card in self.cards:
            cards+=str(card)+"\n"
        return cards
    def __len__(self) -> int:
        """Return the number of cards in the deck"""
        return len(self.cards)
    def serialize(self,filename:str) -> None:
        """Serialize the deck to a file"""
        with open(filename,'w') as f:
            d={}
            cards=[]
            for card in self.cards:
                cards.append(card.to_dict())
            d['cards']=cards
            json.dump(d,f)
    @staticmethod
    def deserialize(filename:str):
        """Deserialize a deck from a file"""
        with open(filename,'r') as f:
            d=json.load(f)
            cards=[]
            for card in d['cards']:
                cards.append(Card.from_dict(card))
            return Deck(cards)
    def get_random_card(self) -> Card:
        """Return a random card from the deck"""
        return self.cards[random.randint(0,len(self.cards)-1)]