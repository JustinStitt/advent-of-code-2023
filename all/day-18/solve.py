#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 18
import sys
import itertools
import functools
import re
from icecream import ic
from collections import defaultdict

NORTH, EAST, SOUTH, WEST = (0, 1, 2, 3)


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]
            self.rows = len(self.lines)
            self.cols = len(self.lines[0])

    def solve(self):
        instrs = []
        for line in self.lines:
            dir, amnt, color = line.split(" ")
            amnt = int(amnt)
            color = color[1:-1]
            # ic(line)
            # ic(dir, amnt, color)
            instrs.append([dir, amnt, color])

        m = []
        num = 10000  # TODO: make bigger for big.in
        for _ in range(num):
            m.append(["."] * num)

        r = num // 2
        c = num // 2

        dir_to_delta = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
        # go dig
        for dir, amnt, color in instrs:
            m[r][c] = "#"  # dig out our feet
            dr, dc = dir_to_delta[dir]
            # move
            for _ in range(amnt):
                r += dr
                c += dc
                m[r][c] = "#"

        # find a traped '.'
        trapped = None
        for idx, row in enumerate(m):
            as_str = "".join(row)
            match = re.search(r"#\.+#", as_str)
            if match:
                trapped = [idx, match.start() + 1]
                break
        assert trapped, 'couldnt find trapped "."'
        # dfs from trapped and dig out
        stk = [trapped]
        while len(stk):
            curr = stk.pop()
            ic(curr)
            ch = m[curr[0]][curr[1]]
            if ch == "#":  # already filled in
                continue
            m[curr[0]][curr[1]] = "#"

            # go to neighbors
            _deltas = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            for delta in _deltas:
                nr, nc = (curr[0] + delta[0], curr[1] + delta[1])
                if m[nr][nc] == ".":
                    stk.append([nr, nc])
        total = 0
        for row in m:
            for c in row:
                if c == "#":
                    total += 1
            #     print(c, end="")
            # print()
        print("total: ", total)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
