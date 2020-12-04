import black_jack

def create_deck():

    deck_of_cards = black_jack.Deck()
    shuffled_cards = deck_of_cards.deck_cards()
    return shuffled_cards

def gameplay():

