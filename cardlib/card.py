import random # for random number generation
class Card:
    """
    Class to create a single learning card.
    A card has a front and a back.
    """
    def __init__(self,front,back) -> None:
        self.front = front
        self.back = back
        self.learned = False
        self.id = random.randint(0,1000000)
    def __str__(self) -> str:
        return self.front + " " + self.back
    def __repr__(self) -> str:
        return self.front + " " + self.back
    def __eq__(self,other) -> bool:
        return self.front == other.front and self.back == other.back
    def __hash__(self) -> int:
        return self.id
    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the card.
        Returns: dict
        """
        return {'front':self.front,'back':self.back,'learned':self.learned}
    @staticmethod
    def from_dict(d:dict) -> 'Card':
        """ 
        Creates a card from a dictionary.
        Returns: Card
        """
        return Card(d['front'],d['back'])