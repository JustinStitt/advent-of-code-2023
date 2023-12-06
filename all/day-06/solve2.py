#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 6 pt 2
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

    def go(self, time, dist):
        total = 0
        for t in range(time):
            # hold down for t seconds
            time_left = time - t
            speed = t
            dist_covered_in_time_left = speed * time_left
            if dist_covered_in_time_left > dist:
                total += 1
        return total

    def solve(self):
        times = re.findall(r"\d+", self.lines[0])
        distances = re.findall(r"\d+", self.lines[1])
        assert len(times) == len(distances), "bad len"

        st = int("".join(x for x in times))
        dt = int("".join(x for x in distances))
        total = 1
        total *= self.go(int(st), dt)

        ic(total)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
