#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 8
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

    def solve(self):
        dirs = self.lines[0]
        adj = dict()
        for line in self.lines[2:]:
            c, l, r = re.findall(r"\w{3}", line)
            adj[c] = [l, r]

        # now go
        idx = 0
        curr = "AAA"
        end = "ZZZ"
        total = 0
        while idx <= len(dirs):
            if idx == len(dirs):
                idx = 0
            instr = dirs[idx]
            total += 1
            ic(instr)
            new_curr = adj[curr][0] if instr == "L" else adj[curr][1]
            if new_curr == end:
                print(total)
                exit(0)
            curr = new_curr
            idx += 1


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
