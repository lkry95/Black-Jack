import black_jack

def create_deck():

    deck_of_cards = black_jack.Deck()
    shuffled_cards = deck_of_cards.deck_cards()
    return shuffled_cards

def gameplay():
    deck = create_deck()
    deal_cards = black_jack.Deal(deck)
    dealing_cards = deal_cards.deal_cards(deck)

    player_hand = dealing_cards[1]
    dealer_hand = dealing_cards[0]

    deck = dealing_cards[2]

    calculation = black_jack.Calculation()
    player_points = calculation.point_calc(player_hand)
    dealer_points = calculation.point_calc(dealer_hand)

    print("This is your hand: ")
    print(player_hand)
    print(f'Your points are:  {player_points}')
    print(f"These are the dealer's cards: {dealer_hand[0], dealer_hand[1]}  and another hidden card")

    game_continue = True

    if player_points == 21:
        print("You win!")
        game_continue = False

    while game_continue:
        hit_or_stay = input('Do you want to hit(h) or stay(s)? ')
        if hit_or_stay == 'h':
            player = black_jack.Player()
            player_hit = player.player_hit(player_hand, deck)
            # print(player_hit)
            player_points = player_hit[0]
            if player_points == 21:
                print("You win!")
                game_continue = False
            elif player_points > 21:
                print("You lose!")
                game_continue = False
            print("This is your hand: ")
            print(player_hand)
            print(f'Your points are:  {player_points}')
            print(f"These are the dealer's cards: {dealer_hand[0]}  and another hidden card")
        elif hit_or_stay == 's':
            dealer = black_jack.Dealer()
            dealer_hit = dealer.dealer_hit(dealer_hand, deck)
            dealer_points = dealer_hit[0]
            print(f'Your points are:  {player_points}')
            print(f'This is the dealer hand {dealer_hand}')
            print(f'Dealer points are:  {dealer_points}')

            if player_points > dealer_points:
                print('You win!')
                game_continue = False
            elif dealer_points > 21:
                print('You win!')
                game_continue = False
            else:
                print('You lose!')
                game_continue = False


def game_loop():
    play_again = True
    while play_again:
        gameplay()
        yes_or_no = input("Do you want to play again? ")
        if yes_or_no == 'n':
            play_again = False


game_loop()
