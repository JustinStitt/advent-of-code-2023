#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 19 pt 2
import sys
import itertools
import functools
import re
from icecream import ic
from collections import defaultdict


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end  # incl
        assert (self.start is None and self.end is None) or (self.end >= self.start)

    def __len__(self) -> int:
        if self.start is None and self.end is None:
            return 0
        return self.end - self.start + 1

    def __repr__(self):
        return f"<{self.start}-{self.end}>"


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
        self.workflows = defaultdict(lambda: list())
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
                self.workflows[name].append([cond, dest])

        x, m, a, s = [Range(1, 4000) for _ in range(4)]
        result = self.go(x, m, a, s, "in", 0)
        ic(result)
        print(result)

    def go(self, x, m, a, s, wf, idx):
        if wf == "R" or any([t.start is None for t in [x, m, a, s]]):
            return 0
        if wf == "A":
            ic(x, m, a, s, wf, len(x) * len(m) * len(a) * len(s))
            return len(x) * len(m) * len(a) * len(s)

        # cond, dest = self.workflows[wf]
        cond, dest = self.workflows[wf][idx]
        _x, _m, _a, _s = [Range(r.start, r.end) for r in [x, m, a, s]]
        if "1==1" in cond:
            return self.go(_x, _m, _a, _s, dest, 0)

        rng = locals()["_" + cond[0]]
        assert cond[0] in "xmas", "bad locals"
        val = int(cond[2:])
        # ic(val)
        _strt, _end = (rng.start, rng.end)
        # update range in question
        if val >= rng.end or val <= rng.start:
            # rng.start = None
            # rng.end = None
            return self.go(_x, _m, _a, _s, wf, idx + 1)
        if ">" in cond:  # a>2006 .... <1-4000>   <2007-4000>  & <1-2005>
            rng.start = val + 1  # does pass
            tot = self.go(_x, _m, _a, _s, dest, 0)
            rng.start = _strt
            rng.end = val
            # go failed route
            fl = self.go(_x, _m, _a, _s, wf, idx + 1)
            return tot + fl
        elif "<" in cond:  # a<2006   <1-4000> -> <1-2005>   <2007-4000>
            rng.end = val - 1
            tot = self.go(_x, _m, _a, _s, dest, 0)
            rng.start = val
            rng.end = _end
            fl = self.go(_x, _m, _a, _s, wf, idx + 1)
            return tot + fl


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
