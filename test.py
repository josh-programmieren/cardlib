from cardlib.card import Card
def test_card():
    card=Card(1,1)
    cdict=card.to_dict()
    print(cdict)
    card2=Card.from_dict(cdict)
    print(card2.to_dict())
    print(card2.to_dict()==card.to_dict())
    print(card2.to_dict()==cdict)
if __name__ == '__main__':
    from sys import argv
    if argv[1]=="card":
        test_card()