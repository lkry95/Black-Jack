

class Deck:

    def __init__(self):
        pass






class Deal:

    def __init__(self, deck):
        self.deck = deck

    # A function for creating player and dealers hands
    # The player and dealer will get 2 cards initially

    def deal_cards(self, cards):
        dealer = [self.deck.pop(), self.deck.pop()]
        player = [self.deck.pop(), self.deck.pop()]
        return [dealer, player]





class Calculation:

    def __init__(self):
        pass




class Player:

    def __init__(self):
        pass

    def player_hit(self, my_cards, deck):



class Dealer(Player):

    def __init__(self):
        pass




