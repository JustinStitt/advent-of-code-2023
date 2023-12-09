#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 9
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

    def go(self, seq, all_diffs):
        n = len(seq) - 1
        # ic(seq)
        diffs = [0] * n
        has_non_zero = False
        for i in range(n):
            diff = seq[i + 1] - seq[i]
            if diff != 0:
                has_non_zero = True
            diffs[i] = diff

        if has_non_zero:
            all_diffs.append(diffs)
            self.go(diffs, all_diffs)
            return

        all_diffs.append(diffs)

        ic(diffs)

    def find_blank(self, all_diffs, seq):
        all_diffs.insert(0, seq)
        all_diffs.append([0] * 100)
        for i in range(len(all_diffs) - 2, -1, -1):
            # print("here")
            diff = all_diffs[i]
            diff.append(all_diffs[i + 1][-1] + diff[-1])
        # print(all_diffs)
        return all_diffs[0][-1]

    def solve(self):
        total = 0
        for line in self.lines:
            # ic(line)
            seq = [int(x) for x in line.split(" ")]
            all_diffs = []
            self.go(seq, all_diffs)
            # ic(all_diffs)
            ans = self.find_blank(all_diffs, seq)
            ic(ans)
            total += ans
            # exit(0)
        print(total)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
