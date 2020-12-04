from random import shuffle

class Deck:

    def __init__(self):
        pass

    def deck_cards(self):

        result = []
        suit = ['H', 'S', 'D', 'C']
        num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        for i in suit:
            for n in num:
                result.append(i + n)

        # The function will return a shuffled deck with 52 cards
        shuffle(result)

        return result


class Deal:

    def __init__(self, deck):
        self.deck = deck

    # A function for creating player and dealers hands
    # The player and dealer will get 2 cards initially

    def deal_cards(self, deck):
        dealer = [self.deck.pop(), self.deck.pop()]
        player = [self.deck.pop(), self.deck.pop()]
        print([dealer, player,deck])





class Calculation:

    def __init__(self):
        pass

    def point_calc(self, my_cards):

        point = 0
        ace = 0
        for i in my_cards:
            if i[1] in ['T', 'J', 'Q', 'K']:
                point += 10
            elif i[1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                point += int(i[1])
            else:
                point += 11
                ace += 1

        if ace > 0:
            for i in range(0, ace):

                if point > 21:
                    point -= 10

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
        calculate = Calculation
        points = calculate.point_calc(dealer_cards)
        results = [dealer_cards, deck, points]

        while points <= 17:
            results = super().player_hit(dealer_cards, deck)
            points = results[2]


        return results


if __name__ == "__main__":







