#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 16 pt 1
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
            self.been_energized = set()
            self.seen = set()

    # NOTE: might need to add something stopping cycles if they exist
    def dfs(self, r, c, dir):
        if r < 0 or r > self.rows - 1:
            return
        if c < 0 or c > self.cols - 1:
            return
        if (r, c, dir) in self.seen:
            return
        ch = self.m[r][c]
        self.seen.add((r, c, dir))
        self.been_energized.add((r, c))

        if dir in (RIGHT, LEFT) and ch in "-.":
            self.dfs(r, (c + 1) if dir == RIGHT else (c - 1), dir=dir)
            return

        if dir in (UP, DOWN) and ch in "|.":
            self.dfs((r + 1) if dir == DOWN else (r - 1), c, dir=dir)
            return

        if dir in (UP, DOWN) and ch in "-":
            self.dfs(r, c - 1, dir=LEFT)
            self.dfs(r, c + 1, dir=RIGHT)
            return

        if dir in (RIGHT, LEFT) and ch in "|":
            self.dfs(r - 1, c, dir=UP)
            self.dfs(r + 1, c, dir=DOWN)
            return

        if dir == RIGHT and ch in "/":
            self.dfs(r - 1, c, dir=UP)
            return

        if dir == RIGHT and ch in "\\":
            self.dfs(r + 1, c, dir=DOWN)
            return

        if dir == LEFT and ch in "/":
            self.dfs(r + 1, c, dir=DOWN)
            return

        if dir == LEFT and ch in "\\":
            self.dfs(r - 1, c, dir=UP)
            return

        if dir == UP and ch in "/":
            self.dfs(r, c + 1, dir=RIGHT)
            return

        if dir == UP and ch in "\\":
            self.dfs(r, c - 1, dir=LEFT)
            return

        if dir == DOWN and ch in "/":
            self.dfs(r, c - 1, dir=LEFT)
            return

        if dir == DOWN and ch in "\\":
            self.dfs(r, c + 1, dir=RIGHT)
            return

    def solve(self):
        for line in self.m:
            print(line)

        self.dfs(0, 0, RIGHT)
        print(len(self.been_energized))


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
