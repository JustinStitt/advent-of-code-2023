#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 11
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
            assert self.rows == self.cols, "sq"
            self.n = self.rows

    def solve(self):
        col_has = [False] * self.cols
        new_lines = []
        for i, line in enumerate(self.lines):
            for c in range(len(line)):
                if line[c] == "#":
                    col_has[c] = True
            if "#" in line:
                new_lines.append(line)
            else:
                new_lines.append("a" * len(line))

        for i in range(len(col_has) - 1, -1, -1):
            res = col_has[i]
            if res:
                continue
            for r in range(len(new_lines)):
                new_lines[r] = new_lines[r][:i] + ("b") + new_lines[r][i + 1 :]

        ic(new_lines)
        pts = []
        off = 10**6
        ro = 0
        for r in range(len(new_lines)):
            co = 0
            for c in range(len(new_lines[r])):
                ch = new_lines[r][c]
                # ic(ch, ro, co)
                if ch == "b":
                    co += off - 1
                    continue
                elif ch == "a":
                    ro += off - 1
                    break
                elif ch == "#":
                    pts.append([r + ro, c + co])
        ic(pts)

        total = 0
        for u in pts:
            for v in pts:
                if u == v:
                    continue
                dist = abs(u[0] - v[0]) + abs(u[1] - v[1])
                total += dist
        # ic(total // 2)
        print(total // 2)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
