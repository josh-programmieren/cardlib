from cardlib.card import Card
from cardlib.deck import Deck
def test_card():
    card=Card("Queen","Hearts")
    cdict=card.to_dict()
    print(cdict)
    card2=Card.from_dict(cdict)
    print(card2.to_dict())
    print(card2.to_dict()==card.to_dict())
    print(card2.to_dict()==cdict)
    return card,card2
def test_deck():
    card1,card2=test_card()
    deck=Deck([card1,card2])
    print(deck)
    deck.serialize('deck.json')
    deck2=Deck.deserialize('deck.json')
    print(deck2)
if __name__ == '__main__':
    from sys import argv
    if argv[1]=="card":
        test_card()
    elif argv[1]=="deck":
        test_deck()
    elif argv[1]=="all":
        test_card()
        test_deck()
    else:
        print("Usage: python3 test.py [card|deck]")