#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 7 pt 2
import sys
import itertools
import functools
import re
from icecream import ic
from collections import defaultdict


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]
            self.rows = len(self.lines)
            self.cols = len(self.lines[0])

    def solve(self):
        old = "AKQJT98765432"
        value = "ZYX0V98765432"
        hands = []
        for line in self.lines:
            hand, bid = line.split(" ")
            bid = int(bid)
            for c in hand:
                idx = old.index(c)
                hand = hand.replace(old[idx], value[idx])
            hands.append(HandSorter(hand, bid))

        # ic(hands)
        hands = sorted(hands, reverse=True)
        # ic(hands)
        total = 0
        for r, h in enumerate(hands):
            m = h.bid * (r + 1)
            ic(h.hand, h.bid)
            ic(m, r + 1, h)
            total += m
            print(h.hand)

        print(total)


def get_hand_strength(hand):
    if "0" in hand:
        return min([get_hand_strength(hand.replace("0", c)) for c in "ZYXV98765432"])
    if len(set(hand)) == 1:
        return 0
    f = defaultdict(lambda: int())
    for c in hand:
        f[c] += 1
    if len(f) == 2:
        if f[hand[0]] == 4 or f[hand[0]] == 1:
            return 1
        if f[hand[0]] == 3 or f[hand[0]] == 2:
            return 2
    if len(f) == 3:
        for k, v in f.items():
            if v == 3:
                return 3
        return 4
    if len(f) == 4:
        return 5
    return 6


class HandSorter:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.strength = get_hand_strength(hand)

    def __repr__(self):
        return f"{self.hand} | {self.bid}"

    def __lt__(self, other):
        hand1 = self.hand
        hand2 = other.hand
        r1 = self.strength
        r2 = get_hand_strength(hand2)

        if r1 < r2:
            return True
        if r1 > r2:
            return False
        assert len(hand1) == len(hand2), "bad len"
        # eq
        for idx in range(len(hand1)):
            u, v = hand1[idx], hand2[idx]
            if u < v:
                return False
            if u > v:
                return True

        return True


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
