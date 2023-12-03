#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 3 pt 1
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

    def is_alone(self, sr, sc, l):
        sir = sr - 1
        sic = sc - 1
        eir = sr + 1
        eic = sc + l

        for r in range(sir, eir + 1):
            for c in range(sic, eic + 1):
                if r < 0 or c < 0:
                    continue
                if r > self.rows - 1 or c > self.cols - 1:
                    continue
                if r == sr and c in range(sc, sc + l):  # is num itself
                    continue
                if self.lines[r][c] != "." and not self.lines[r][c].isdigit():
                    return False
        return True

    def solve(self):
        total = 0
        for r, line in enumerate(self.lines):
            ic(line)
            matches = [(x.start(), x.end()) for x in re.finditer(r"\d+", line)]
            for _strt, _end in matches:
                l = _end - _strt
                res = self.is_alone(r, _strt, l)
                if not res:
                    total += int(line[_strt:_end])

        ic(total)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
