from typing import List, Dict
from utils.utils import timeit
from collections import defaultdict


@timeit
def solveA(input_data: List[str]) -> int:
    hands = obtain_hands(input_data)
    return calculate_winnings(hands)


@timeit
def solveB(input_data: List[str]) -> int:
    hands = obtain_hands_with_joker(input_data)
    return calculate_winnings(hands)


def obtain_hands(input_data):
    hands = []
    for line in input_data:
        hand, bid = line.split()
        hands.append(Hand(hand, int(bid)))
    return hands


def obtain_hands_with_joker(input_data):
    hands = []
    for line in input_data:
        hand, bid = line.split()
        hands.append(HandWithJoker(hand, int(bid)))
    return hands


def calculate_winnings(hands):
    sorted_hands = sorted(hands)
    winnings = 0
    for i, hand in enumerate(sorted_hands):
        winnings += hand.bid * (i + 1)
    return winnings


class Hand:
    def __init__(self, hand_string: str, bid: int = 0) -> None:
        self.cards = list(hand_string)
        self.strength = self.get_strength()
        self.bid = bid

    def __repr__(self):
        return f"Cards: {self.cards}\n Str: {self.strength}\n Bid: {self.bid}"

    def __lt__(self, other: "Hand"):
        return self.compare_with(other) == -1

    def __eq__(self, other: "Hand"):  # type: ignore[override]
        return self.compare_with(other) == 0

    def __gt__(self, other: "Hand"):
        return self.compare_with(other) == 1

    def card_value(self, card: str):
        order = "AKQJT98765432"
        return order.index(card)

    def get_strength(self) -> int:
        return self.hand_strength()

    def hand_strength(self) -> int:
        counts: Dict[str, int] = defaultdict(int)
        for card in self.cards:
            counts[card] += 1

        values = sorted(counts.values(), reverse=True)
        if values == [5]:
            return 7
        elif values == [4, 1]:
            return 6
        elif values == [3, 2]:
            return 5
        elif values == [3, 1, 1]:
            return 4
        elif values == [2, 2, 1]:
            return 3
        elif values == [2, 1, 1, 1]:
            return 2
        else:
            return 1

    def compare_with(self, other_hand: "Hand") -> int:
        if self.strength > other_hand.strength:
            return 1
        elif self.strength < other_hand.strength:
            return -1
        else:
            for i in range(5):
                value_self = self.card_value(self.cards[i])
                value_other = other_hand.card_value(other_hand.cards[i])
                if value_self < value_other:
                    return 1
                elif value_self > value_other:
                    return -1
        return 0


class HandWithJoker(Hand):
    def card_value(self, card: str):
        order = "AKQT98765432J"
        return order.index(card)

    def hand_strength(self) -> int:
        counts: Dict[str, int] = defaultdict(int)
        for card in self.cards:
            counts[card] += 1

        joker_count = counts["J"]
        del counts["J"]

        values = sorted(counts.values(), reverse=True)
        if values:
            values[0] += joker_count
        else:
            values = [joker_count]

        if values == [5]:
            return 7
        elif values == [4, 1]:
            return 6
        elif values == [3, 2]:
            return 5
        elif values == [3, 1, 1]:
            return 4
        elif values == [2, 2, 1]:
            return 3
        elif values == [2, 1, 1, 1]:
            return 2
        else:
            return 1
