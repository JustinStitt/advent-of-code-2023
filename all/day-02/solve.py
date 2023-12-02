#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 2
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

        self.red_lim = 12
        self.green_lim = 13
        self.blue_lim = 14

    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    def solve(self):
        total = 0
        for line in self.lines:
            ic(line)
            _id = int(re.findall(r"\d+", line)[0])
            line = line.split(";")
            ic(_id, line)
            bad = False
            for round in line:
                red_matches = re.findall(r"\d+(?= red)", round)
                green_matches = re.findall(r"\d+(?= green)", round)
                blue_matches = re.findall(r"\d+(?= blue)", round)

                red, green, blue = [0] * 3
                if len(red_matches):
                    red = red_matches[0]

                if len(green_matches):
                    green = green_matches[0]

                if len(blue_matches):
                    blue = blue_matches[0]

                if (
                    int(red) > self.red_lim
                    or int(green) > self.green_lim
                    or int(blue) > self.blue_lim
                ):
                    bad = True
                    ic("bad")
                    ic(_id, line, red, green, blue)

            total += 0 if bad else _id
        print(total)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
