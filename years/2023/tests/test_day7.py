import unittest
from days.day7 import solveA, solveB, obtain_hands, Hand, HandWithJoker

from utils.utils import list_string_parser


class ExternalFunctions(unittest.TestCase):
    def test_example_1(self):
        input_data = list_string_parser("data/example_day7.txt")
        expected_output = 6440

        self.assertEqual(solveA(input_data), expected_output)

    def test_part_1(self):
        input_data = list_string_parser("data/day7.txt")
        expected_output = 253954294

        self.assertEqual(solveA(input_data), expected_output)

    def test_example_2(self):
        input_data = list_string_parser("data/example_day7.txt")
        expected_output = 5905

        self.assertEqual(solveB(input_data), expected_output)

    def test_part_2(self):
        input_data = list_string_parser("data/day7.txt")
        expected_output = 254837398

        self.assertEqual(solveB(input_data), expected_output)


class InternalFunctions(unittest.TestCase):
    def test_obtain_hands(self):
        input_data = ["32T3K 765"]
        expected_cards = ["32T3K"]
        expected_bid = 765
        hands = obtain_hands(input_data)
        self.assertEqual(hands[0].cards, list(expected_cards[0]))
        self.assertEqual(hands[0].bid, expected_bid)

    def test_hand(self):
        hand1 = Hand("33332")
        hand2 = Hand("2AAAA")
        result = hand1.compare_with(hand2)
        self.assertEqual(result, 1)

    def test_equal_hands(self):
        hand1 = Hand("32T3K")
        hand2 = Hand("32T3K")
        self.assertEqual(hand1, hand2)

    def test_gt(self):
        hand1 = Hand("33332")
        hand2 = Hand("2AAAA")
        self.assertTrue(hand1 > hand2)

    def test_lt(self):
        hand1 = Hand("77788")
        hand2 = Hand("77888")
        self.assertTrue(hand1 < hand2)

    def test_sort_hands(self):
        hands = [
            Hand("32T3K"),
            Hand("T55J5"),
            Hand("KK677"),
            Hand("KTJJT"),
            Hand("QQQJA"),
        ]

        sorted_hands = sorted(hands)
        self.assertEqual(sorted_hands[0], Hand("32T3K"))
        self.assertEqual(sorted_hands[1], Hand("KTJJT"))
        self.assertEqual(sorted_hands[2], Hand("KK677"))
        self.assertEqual(sorted_hands[3], Hand("T55J5"))
        self.assertEqual(sorted_hands[4], Hand("QQQJA"))

    def test_hand_with_joker(self):
        hand1 = HandWithJoker("JKKK2")
        hand2 = HandWithJoker("QQQQ2")
        result = hand1.compare_with(hand2)
        self.assertEqual(result, -1)

    def test_sort_hands_with_joker(self):
        hands = [
            HandWithJoker("32T3K"),
            HandWithJoker("T55J5"),
            HandWithJoker("KK677"),
            HandWithJoker("KTJJT"),
            HandWithJoker("QQQJA"),
        ]

        sorted_hands = sorted(hands)
        self.assertEqual(sorted_hands[0], HandWithJoker("32T3K"))
        self.assertEqual(sorted_hands[1], HandWithJoker("KK677"))
        self.assertEqual(sorted_hands[2], HandWithJoker("T55J5"))
        self.assertEqual(sorted_hands[3], HandWithJoker("QQQJA"))
        self.assertEqual(sorted_hands[4], HandWithJoker("KTJJT"))
