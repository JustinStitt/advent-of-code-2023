#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 8 pt 2 (try 2 lol)
import sys
import itertools
import functools
import re
from math import lcm

# from icecream import ic
from collections import defaultdict

ic = lambda *args: int()


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]
            self.rows = len(self.lines)
            self.cols = len(self.lines[0])

    def solve(self):
        dirs = self.lines[0]
        adj = dict()
        starting = []
        ending = []
        for line in self.lines[2:]:
            c, l, r = re.findall(r"[A-Z\d]{3}", line)
            ic(c, l, r)
            adj[c] = [l, r]
            if c[-1] == "A":
                starting.append(c)
            elif c[-1] == "Z":
                ending.append(c)
        ic(starting, ending)
        # now go
        # currs = starting[::]
        # total = 0
        mults = []
        for sp in starting:
            curr = sp
            total = 0
            idx = 0
            while idx <= len(dirs):
                if idx == len(dirs):
                    idx = 0
                instr = dirs[idx]
                instr = 0 if instr == "L" else 1
                total += 1
                curr = adj[curr][instr]
                if curr[-1] == "Z":
                    mults.append(total)
                    break

                idx += 1

        res = lcm(*mults)
        print(res)


# fmt: off
if __name__ == "__main__":
    # if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    # else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
