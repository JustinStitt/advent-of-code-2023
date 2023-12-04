#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 4 pt 1
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
        total = 0
        card_freq = defaultdict(lambda: int())
        card_val = defaultdict(lambda: int())
        hits = defaultdict(lambda: int())
        for i, l in enumerate(self.lines):
            card_freq[i] += 1

        idx = 0
        while idx < len(self.lines) and card_freq[idx] > 0:
            hits[idx] += 1
            line = self.lines[idx]
            line = line.split(":")[1]
            line = line.split("|")
            matches = 0
            winning = [x for x in line[0].split(" ") if len(x)]
            ours = [x for x in line[1].split(" ") if len(x)]
            for i, v in enumerate(ours):
                if v in winning:
                    matches += 1
            # win the next 'matches' cards
            for y in range(idx + 1, idx + 1 + matches):
                card_freq[y] += 1
            # ic(card_freq)
            card_freq[idx] -= 1
            if card_freq[idx] == 0:
                idx += 1
        ic(sum(hits.values()))


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
