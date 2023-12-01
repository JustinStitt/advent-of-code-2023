#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 1 pt 2
import sys
import itertools
import functools
import re
from icecream import ic
from collections import defaultdict

spelled_out = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]

    def solve(self):
        total = 0
        s = ""
        for line in self.lines:
            ic(line)
            for idx, so in enumerate(spelled_out):
                while so in line:
                    i = line.index(so)
                    line = line[: i + 1] + str(idx + 1) + line[i + 2 :]
                # line = line.replace(so, str(idx + 1))
            ic(line)
            for c in line:
                if c >= "0" and c <= "9":
                    s += c
                    break
            for c in line[::-1]:
                if c >= "0" and c <= "9":
                    s += c
                    break
            total += int(s)
            ic(int(s))
            s = ""
        print(total)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
