#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 21
import sys
import itertools
import functools
import re
from icecream import ic
from collections import defaultdict
import sys

sys.setrecursionlimit(10**8)


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]
            self.rows = len(self.lines)
            self.cols = len(self.lines[0])
            self.m = self.lines
            self.deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            self.pts = set()

    @functools.lru_cache(maxsize=None)
    def go(self, r, c, limit):
        if self.m[r % self.rows][c % self.cols] == "#":
            return False

        if limit == 0:
            self.pts.add((r, c))
            return False

        for dr, dc in self.deltas:
            nr = r + dr
            nc = c + dc
            res = self.go(nr, nc, limit - 1)
            if res == True:
                return True

        return False

    def solve(self):
        start = [self.rows // 2, self.cols // 2]
        ic(start)
        # new idea: start at pt, try to get to S with 64 moves
        # 64, 195, 326
        limit = 327  # bump to 128 from 64 to test tesselation
        total = 0
        res = self.go(start[0], start[1], limit)
        total += 1 if res else 0
        print(len(self.pts))
        # print(f"{limit = } <--> {total = }")


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
