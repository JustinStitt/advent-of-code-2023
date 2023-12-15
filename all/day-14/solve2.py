#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 14 pt 2
import sys
import itertools
import functools
import re
from icecream import ic
from collections import defaultdict
from numpy_cache import np_cache
import numpy as np

CYCLES = 1000000000


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]
            self.rows = len(self.lines)
            self.cols = len(self.lines[0])

    def move_then_get_state(self, mat, dir='north'):
        if dir in ("north", "west"):
            for r, row in enumerate(mat):
                for c, ch in enumerate(row):
                    if ch != "O": continue
                    # if up
                    if dir == 'north':
                        curr_row = r
                        while True:
                            if curr_row <= 0:
                                break
                            if mat[curr_row-1][c] != '.':
                                break
                            mat[curr_row-1][c] = "O"
                            mat[curr_row][c] = "."
                            curr_row -= 1
                    elif dir == 'west':
                        curr_col = c
                        while True:
                            if curr_col <= 0:
                                break
                            if mat[r][curr_col-1] != ".":
                                break
                            mat[r][curr_col-1] = 'O'
                            mat[r][curr_col] = '.'
                            curr_col -= 1
        else:
            for r in range(len(mat)-1, -1, -1):
                row = mat[r]
                # ic(row)
                for c in range(len(row)-1,-1,-1):
                    col = row[c]
                    ch = col
                    if ch != "O": continue
                    if dir == 'east':
                        curr_col = c
                        while True:
                            if curr_col >= len(mat[0]) - 1:
                                break
                            if mat[r][curr_col+1] != ".":
                                break
                            mat[r][curr_col+1] = 'O'
                            mat[r][curr_col] = '.'
                            curr_col += 1
                    elif dir == 'south':
                        curr_row = r
                        while True:
                            if curr_row >= len(mat)-1:
                                break
                            if mat[curr_row+1][c] != '.':
                                break
                            mat[curr_row+1][c] = 'O'
                            mat[curr_row][c] = '.'
                            curr_row += 1

        state = ""
        for row in mat:
            state += ''.join(row)
        return state





    # def move
    # num empty above or wall or # - round rocks above
    def solve(self):
        self.lines = [list(x) for x in self.lines]
        ic(self.lines)
        self.move_then_get_state(self.lines)
        ic(self.lines)
        ...
        seen = dict()
        cycle_len = None
        last_k = None
        for cycle in range(1, CYCLES+1):#CYCLES):
            state = None
            for dir in ("north", "west", "south", "east"):
                state = self.move_then_get_state(self.lines, dir=dir)
                ic(dir, self.lines)
            assert state, 'bad state'
            if state in seen:
                ic('repeat state hit at: ', state, ' and', cycle)
                cycle_len = cycle-seen[state]
                last_k = cycle
                break
            seen[state] = cycle
        assert cycle_len
        assert last_k
        remaining = CYCLES-last_k
        mod = remaining % cycle_len
        # 105162 too high
        for i in range(mod):
            for dir in ("north", "west", "south", "east"):
                self.move_then_get_state(self.lines, dir=dir)

        # get total laod on beams
        total = 0
        ic(self.lines)
        for r in range(len(self.lines)):
            for c in range(len(self.lines[0])):
                if self.lines[r][c] == 'O':
                    total += len(self.lines) - r
                    ic(r, c, len(self.lines)-r)
        print(total)

                # ic(dir, self.lines)
        # arr = (np.asarray([list(x) for x in self.lines]))
        # ic(arr)
        # rot = np.rot90(arr)
        # ic(rot)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
