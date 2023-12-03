#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 3 pt 2
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
                if (
                    self.lines[r][c] != "."
                    and not self.lines[r][c].isdigit()
                    and self.lines[r][c] == "*"
                ):
                    return [r, c]
        return [None, None]

    def solve(self):
        total = 0
        gear_map = defaultdict(lambda: int(1))
        gear_freq = defaultdict(lambda: int())
        for r, line in enumerate(self.lines):
            ic(line)
            matches = [(x.start(), x.end()) for x in re.finditer(r"\d+", line)]
            for _strt, _end in matches:
                l = _end - _strt
                gr, gc = self.is_alone(r, _strt, l)
                if gr is not None and gc is not None:
                    gear_map[(gr, gc)] *= int(line[_strt:_end])
                    gear_freq[(gr, gc)] += 1

        for k in gear_map:
            total += gear_map[k] if gear_freq[k] == 2 else 0
        ic(gear_map)
        ic(gear_freq)
        ic(total)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
