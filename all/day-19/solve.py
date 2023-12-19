#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 19
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

    def det(self, x, m, a, s, cond, dest):
        # ic(x, m, a, s)
        # ic(cond, dest)
        result = eval(cond)
        # ic(result)
        if result == True:
            if dest == "A":
                return True
            if dest == "R":
                return False
            return dest
        return None

    def solve(self):
        workflows = defaultdict(lambda: list())
        parts = []
        bidx = self.lines.index("")
        for line in self.lines[:bidx]:
            inner = re.search(r"{.*}", line)
            assert inner, "no match"
            name = line[: inner.start()]
            inner = inner.group()[1:-1]
            pieces = inner.split(",")
            for piece in pieces:
                if ":" in piece:
                    cond, dest = piece.split(":")
                else:
                    cond = "1==1"
                    dest = piece
                workflows[name].append([cond, dest])
        ic(workflows)

        accepted = 0
        for line in self.lines[bidx + 1 :]:
            wf = "in"
            # 'in': [['s<1351', 'px'], ['1==1', 'qqz']],

            numbers = re.findall(r"\d+", line)
            x, m, a, s = [int(x) for x in numbers]
            # cond, dest = parts[0]
            result = None
            ic(x, m, a, s)
            while result not in (False, True):
                for cond, dest in workflows[wf]:
                    result = self.det(x, m, a, s, cond, dest)
                    ic(wf, result, cond, dest)
                    if result is None:
                        continue
                    if result is True:  # accepted
                        accepted += x + m + a + s
                        break
                    if result is False:  # rejected
                        break
                    wf = result
                    break

        print(accepted)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
