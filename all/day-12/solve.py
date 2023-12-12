#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 12
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

    def is_valid(self, puzzle, nums):
        runs = []
        i = 0
        n = len(puzzle)
        in_run = None
        run_start = 0
        while i < n:
            if puzzle[i] == "#":
                if in_run is False:
                    run_start = i
                in_run = True
            elif puzzle[i] == ".":
                if in_run:
                    run_length = i - run_start
                    runs.append(run_length)
                    # ic(i, run_start, run_length)
                in_run = False
            i += 1
        if in_run:
            runs.append(i - run_start)

        # ic(runs)
        # ic(nums)
        return runs == nums

    def go(self, puzzle, nums):
        puzzle = list(puzzle)
        idks = []
        for i in range(len(puzzle)):
            if puzzle[i] == "?":
                idks.append(i)
        ceiling = 2 ** (len(idks))

        works = 0
        for i in range(ceiling):
            zfilled = bin(i)[2:].zfill(len(idks))
            # reconstruct puzzle
            for j in range(len(zfilled)):
                idx = idks[j]
                puzzle[idx] = "#" if zfilled[j] == "1" else "."
            if self.is_valid("".join(puzzle), nums):
                works += 1
        # ic(idks)
        ic(works)
        return works

    def solve(self):
        total = 0
        for idx, line in enumerate(self.lines):
            print(f"on line: {idx}: {line}", flush=True)
            puzzle, nums = line.split(" ")
            nums = [int(x) for x in nums.split(",")]
            ret = self.go(puzzle, nums)
            total += ret
            # ic(puzzle * 5, nums * 5)
        # ic(self.is_valid(".#.###.#.######", [1, 3, 1, 6]))
        print(total)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
