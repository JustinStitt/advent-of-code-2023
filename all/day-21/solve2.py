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
            self.deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    @functools.lru_cache(maxsize=1024)
    def go(self, r, c, goal_r, goal_c, limit):
        if r < 0 or r > self.rows - 1:
            return False

        if c < 0 or c > self.cols - 1:
            return False

        if self.m[r][c] == "#":
            return False

        if r == goal_r and c == goal_c and limit == 0:
            return True

        if limit <= 0:
            return False

        for dr, dc in self.deltas:
            nr = r + dr
            nc = c + dc
            res = self.go(nr, nc, goal_r, goal_c, limit - 1)
            if res == True:
                return True

        return False

    def solve(self):
        m = self.m
        patt = r"(O.*O)"
        tips = 2
        max_area = 65 * 65
        rock_count = 0
        O_count = tips
        for line in self.m:
            matches = re.findall(patt, line)
            assert len(matches) == 1 or len(matches) == 0, "bad matches count"
            ic(matches)
            if len(matches):
                match = matches[0]
                rock_count += match.count("#")
                O_count += match.count("O")

        realized = max_area - rock_count
        ic(max_area, rock_count, realized)
        ic(realized // 2)
        ic(O_count)
        density = O_count / max_area
        ic(density)  # 0.8676923076923077

        # m = self.m
        # start = [-1, -1]
        # for r, row in enumerate(m):
        #     for c, col in enumerate(row):
        #         if col == "S":
        #             start = [r, c]

        # ic(start)
        # # new idea: start at pt, try to get to S with 64 moves
        # total = 0
        # limit = 64
        # for r, row in enumerate(m):
        #     for c, col in enumerate(row):
        #         # if r == start[0] and c == start[1]:
        #         #     continue
        #         res = self.go(r, c, start[0], start[1], limit)
        #         if res:
        #             print("O", end="")
        #         else:
        #             print(m[r][c], end="")
        #         total += 1 if res else 0
        #     print()

        # print("res: ", total)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
