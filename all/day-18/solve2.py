#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 18 pt 2
import sys
import itertools
import functools
import re
from icecream import ic
from collections import defaultdict
from shapely.geometry import Polygon

NORTH, EAST, SOUTH, WEST = (0, 1, 2, 3)


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]
            self.rows = len(self.lines)
            self.cols = len(self.lines[0])

    def test(self):
        coords = [(0, 0), (5, 0), (5, 5), (0, 5)]
        pgon = Polygon(coords)
        print(pgon.area)

    def solve(self):
        instrs = []
        num_to_dir = {0: "R", 1: "D", 2: "L", 3: "U"}
        for line in self.lines:
            dir, amnt, color = line.split(" ")
            amnt = int(amnt)
            color = color[2:-1]
            # ic(line)
            # ic(dir, amnt, color)
            amnt = int(color[:-1], base=16)
            dir = int(color[-1])
            dir = num_to_dir[dir]
            ic(amnt, dir)
            instrs.append([dir, amnt, color])

        dir_to_delta = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
        cpt = (0, 0)
        curr = [0, 0]
        pts = [cpt]
        # go dig
        for dir, amnt, color in instrs:
            dr, dc = dir_to_delta[dir]
            dr *= amnt
            dc *= amnt
            curr = [curr[0] + dc, curr[1] + dr]
            pts.append(tuple(curr))
        trenchline = 0
        for a, b in zip(pts[::2], pts[1::2]):
            dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
            trenchline += dist
        pgon = Polygon(pts)
        ic(pts)
        ic(pgon.area, trenchline)
        print(pgon.area + (pgon.length // 2 + 1))
        print(pgon.length)
        # 952404941483 + (6405262/2+1)
        # ic(pts)

        # for y, row in enumerate(m):
        #     for x, col in enumerate(row):
        #         if (x, y) in pts:
        #             print("#", end="")
        #         else:
        #             print(".", end="")
        #     print()


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
    # soln.test()
