#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 14
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

    # num empty above or wall or # - round rocks above
    def solve(self):
        total = 0
        for row, line in enumerate(self.lines):
            for i in range(len(line)):
                if line[i] != "O":
                    continue
                # try to move up
                curr_row = row
                cnt = 0
                while True:
                    if curr_row == 0:
                        break
                    if self.lines[curr_row - 1][i] == "#":
                        break
                    if self.lines[curr_row - 1][i] == "O":
                        cnt += 1
                    curr_row -= 1
                score = self.rows - curr_row - cnt
                ic(score)
                total += score
        ic(self.lines)
        ic(total)
        print(total)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
