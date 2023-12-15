#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 15
import sys
import itertools
import functools
import re
from icecream import ic
from collections import defaultdict


def HASH(s: str):
    curr = 0
    for c in s:
        ascii = ord(c)
        curr += ascii
        curr *= 17
        curr %= 256
    return curr


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]
            self.rows = len(self.lines)
            self.cols = len(self.lines[0])

    def solve(self):
        seq = self.lines[0].split(",")
        _sum = 0
        for item in seq:
            hsh = HASH(item)

            _sum += hsh

        # ic(seq)
        # ic(_sum)
        print(_sum)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
