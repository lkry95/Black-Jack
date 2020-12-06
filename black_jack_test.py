import unittest
import black_jack

class TestDeck(unittest.TestCase):
    def test_deckcards(self):

        expected_list = [
            'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CT', 'CJ', 'CQ', 'CK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DT', 'DJ', 'DQ', 'DK',
            'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'HT', 'HJ', 'HQ', 'HK',
            'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK',
            ]
        testing_class = black_jack.Deck()
        self.assertEqual(testing_class.deck_cards().sort(), expected_list.sort())

    def test_deal_cards(self):

        deck = [
            'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CT', 'CJ', 'CQ', 'CK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DT', 'DJ', 'DQ', 'DK',
            'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'HT', 'HJ', 'HQ', 'HK',
            'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK',
        ]

        test_class = black_jack.Deal(deck)
        num_cards = test_class.deal_cards(deck)
        self.assertEqual(len(num_cards), 3)
        self.assertEqual(len(num_cards[0]), 2)
        self.assertEqual(len(num_cards[1]), 2)
        self.assertEqual(len(num_cards[2]), 48)

    def test_point_calc(self):

        lst = ['H9', 'C3', 'S4']
        test_class = black_jack.Calculation()
        total_points = test_class.point_calc(lst)
        self.assertEqual(total_points, 16)

        lst = ['HA', "DA", 'C9']
        test_class = black_jack.Calculation()
        total_points = test_class.point_calc(lst)
        self.assertEqual(total_points, 21)

        lst = ['H4', 'H3', "DT", "SQ"]
        test_class = black_jack.Calculation()
        total_points = test_class.point_calc(lst)
        self.assertEqual(total_points, 27)

