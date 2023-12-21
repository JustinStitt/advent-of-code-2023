#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 21
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
            self.m = self.lines

    def solve(self):
        m = self.m
        start = [-1, -1]
        for r, row in enumerate(m):
            for c, col in enumerate(row):
                if col == "S":
                    start = [r, c]

        ic(start)

        max_steps = 64
        # bfs
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        Q = [(start, 0)]
        seen_steps = set()

        done = []
        while len(Q):
            curr = Q.pop(0)
            pos, steps = curr
            if steps not in seen_steps:
                seen_steps.add(steps)
                print("step depth: ", steps)
            if steps >= max_steps:
                done.append(pos)
                continue
            assert pos, "bad pos"
            r, c = pos
            ic(r, c, steps)

            # add neighbors
            for dr, dc in deltas:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr > self.rows - 1:
                    continue
                if nc < 0 or nc > self.cols - 1:
                    continue
                if m[nr][nc] != ".":
                    continue
                Q.append(([nr, nc], steps + 1))  # type: ignore

        ic(Q)
        res = set()
        for item in done:
            pos = item
            r, c = pos
            res.add((r, c))
        print("answer: ", len(res))
        exit(0)
        for r, row in enumerate(m):
            for c, col in enumerate(row):
                if (r, c) in res:
                    print("O", end="")
                else:
                    print(m[r][c], end="")
            print()


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
