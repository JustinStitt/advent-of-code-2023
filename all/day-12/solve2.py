#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 12 pt2
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

    @functools.lru_cache(None)
    def go(self, idx, secidx, curr):
        ic(idx, secidx, curr)
        puzzle = self.puzzle
        nums = self.nums
        n, m = len(puzzle), len(nums)
        if idx == n:
            if secidx == m and curr == 0:
                ic("here")
                return 1
            elif secidx == m - 1 and nums[secidx] == curr:
                ic("here2")
                return 1
            else:
                return 0
        ans = 0
        ch = puzzle[idx]
        if ch == "." or ch == "?":
            if curr == 0:
                ans += self.go(idx + 1, secidx, 0)
            elif curr > 0 and secidx < m and nums[secidx] == curr:
                ans += self.go(idx + 1, secidx + 1, 0)
            elif ch == "?":
                ans += self.go(idx + 1, secidx, curr + 1)

        if ch == "#" or ch == "?":
            if "#" == "." and curr == 0:
                ans += self.go(idx + 1, secidx, 0)
            elif "#" == "." and curr > 0 and secidx < m and nums[secidx] == curr:
                ans += self.go(idx + 1, secidx + 1, 0)
            elif "#" == "#":
                ans += self.go(idx + 1, secidx, curr + 1)
        return ans

    def solve(self):
        total = 0
        for idx, line in enumerate(self.lines):
            print(f"on line: {idx}: {line}", flush=True)
            puzzle, nums = line.split(" ")
            nums = [int(x) for x in nums.split(",")]

            new_puzzle = "?".join([puzzle, puzzle, puzzle, puzzle, puzzle])
            self.puzzle = new_puzzle
            self.nums = nums * 5
            ret = self.go(0, 0, 0)
            ic(self.puzzle, self.nums)
            ic(ret)
            total += ret
            self.go.cache_clear()
            # ic(puzzle * 5, nums * 5)
        # ic(self.is_valid(".#.###.#.######", [1, 3, 1, 6]))
        print(total)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
