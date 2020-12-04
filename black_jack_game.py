import black_jack

def create_deck():

    deck_of_cards = black_jack.Deck()
    shuffled_cards = deck_of_cards.deck_cards()
    return shuffled_cards

def gameplay():
    deck = create_deck()
    deal_cards = black_jack.Deal()
    dealing_cards = deal_cards.deal_cards(deck)

    # player_hand = []
    # dealer_hand = []

    player_hand = dealing_cards[1]
    dealer_hand = dealing_cards[0]

    deck = dealing_cards[2]

    calculation = black_jack.Calculation()
    player_points = calculation.point_calc(player_hand)
    dealer_points = calculation.point_calc(dealer_hand)

    print("This is your hand: ")
    print(player_hand)
    print(f'Your points are:  {player_points}')
    print(f"These are the dealer's cards: {dealer_hand[0]}  and another hidden card")


    game_continue = True

    if player_points == 21:
        print("You win!")
        game_continue = False

    while game_continue:


