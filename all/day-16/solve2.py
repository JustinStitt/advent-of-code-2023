#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 16 pt 2
import sys
import itertools
import functools
import re
from icecream import ic
from collections import defaultdict

sys.setrecursionlimit(10**9)
UP, DOWN, LEFT, RIGHT = (0, 1, 2, 3)


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]
            self.rows = len(self.lines)
            self.cols = len(self.lines[0])
            self.m = self.lines
            self.seen = set()
            self.best_energy = -(10**18)

    # NOTE: might need to add something stopping cycles if they exist
    def dfs(self, r, c, dir, e, s):
        if r < 0 or r > self.rows - 1:
            return
        if c < 0 or c > self.cols - 1:
            return
        if (r, c, dir) in s:
            return
        ch = self.m[r][c]
        s.add((r, c, dir))
        e.add((r, c))

        if dir in (RIGHT, LEFT) and ch in "-.":
            self.dfs(r, (c + 1) if dir == RIGHT else (c - 1), dir, e, s)
            return

        if dir in (UP, DOWN) and ch in "|.":
            self.dfs((r + 1) if dir == DOWN else (r - 1), c, dir, e, s)
            return

        if dir in (UP, DOWN) and ch in "-":
            self.dfs(r, c - 1, LEFT, e, s)
            self.dfs(r, c + 1, RIGHT, e, s)
            return

        if dir in (RIGHT, LEFT) and ch in "|":
            self.dfs(r - 1, c, UP, e, s)
            self.dfs(r + 1, c, DOWN, e, s)
            return

        if dir == RIGHT and ch in "/":
            self.dfs(r - 1, c, UP, e, s)
            return

        if dir == RIGHT and ch in "\\":
            self.dfs(r + 1, c, DOWN, e, s)
            return

        if dir == LEFT and ch in "/":
            self.dfs(r + 1, c, DOWN, e, s)
            return

        if dir == LEFT and ch in "\\":
            self.dfs(r - 1, c, UP, e, s)
            return

        if dir == UP and ch in "/":
            self.dfs(r, c + 1, RIGHT, e, s)
            return

        if dir == UP and ch in "\\":
            self.dfs(r, c - 1, LEFT, e, s)
            return

        if dir == DOWN and ch in "/":
            self.dfs(r, c - 1, LEFT, e, s)
            return

        if dir == DOWN and ch in "\\":
            self.dfs(r, c + 1, RIGHT, e, s)
            return

    def wrap_dfs(self, r, c, dir):
        energized = set()
        seen = set()
        self.dfs(r, c, dir, energized, seen)
        ic(len(energized))
        self.best_energy = max(self.best_energy, len(energized))
        ic(self.best_energy)

    def solve(self):
        for line in self.m:
            print(line)

        # exit(0)
        # starting top row or bottom row
        for sc in range(self.cols):
            tr = 0
            br = self.rows - 1
            self.wrap_dfs(tr, sc, dir=DOWN)
            self.wrap_dfs(br, sc, dir=UP)
            if sc == 0:
                self.wrap_dfs(tr, sc, dir=RIGHT)
                self.wrap_dfs(br, sc, dir=RIGHT)
            if sc == self.cols - 1:
                self.wrap_dfs(tr, sc, dir=LEFT)
                self.wrap_dfs(br, sc, dir=LEFT)

        # starting left col or right col:
        for sr in range(self.rows):
            lc = 0
            rc = self.cols - 1

            self.wrap_dfs(sr, lc, dir=RIGHT)
            self.wrap_dfs(sr, rc, dir=LEFT)
            if sr == 0:
                self.wrap_dfs(sr, lc, dir=DOWN)
                self.wrap_dfs(sr, rc, dir=DOWN)
            if sr == self.rows - 1:
                self.wrap_dfs(sr, lc, dir=UP)
                self.wrap_dfs(sr, rc, dir=UP)

        self.wrap_dfs(0, 6, DOWN)
        print(self.best_energy)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
