from random import shuffle

class Deck:

    def __init__(self):
        pass

    def deck_cards(self):

        deck = []
        suit = ['H', 'S', 'D', 'C']
        num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        for i in suit:
            for n in num:
                deck.append(i + n)

        shuffle(deck)

        return deck


class Deal:

    def __init__(self, deck):
        self.deck = deck



    def deal_cards(self, deck):
        dealer = [self.deck.pop(), self.deck.pop()]
        player = [self.deck.pop(), self.deck.pop()]
        return [dealer, player, deck]


class Calculation:

    def __init__(self):
        pass

    def point_calc(self, my_cards):

        point = 0

        for i in my_cards:
            if i[1] in ['T', 'J', 'Q', 'K']:
                point += 10
            elif i[1] in ['2', '3', '4', '5', '6', '7', '8', '9']:
                point += int(i[1])
            else:
                if point <= 10:
                    point += 11
                else:
                    point += 1


        return point


class Player:

    def __init__(self):
        pass

    def player_hit(self, my_cards, deck):

        my_cards.append(deck.pop())
        calculate = Calculation()
        points = calculate.point_calc(my_cards)
        return (points,my_cards,deck)



class Dealer(Player):

    def __init__(self):
        pass


    def dealer_hit(self, dealer_cards, deck):
        calculate = Calculation()
        points = calculate.point_calc(dealer_cards)
        results = [points, dealer_cards, deck]
        while results[0] < 17:
            results = super().player_hit(dealer_cards, deck)
            points = results[0]


        return results







