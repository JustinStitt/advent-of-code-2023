#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 10 pt 2 (but doesnt work, failed atttempt to render)
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

    def solve(self):
        rows = self.rows
        cols = self.cols
        NORTH = (-1, 0)
        SOUTH = (1, 0)
        EAST = (0, 1)
        WEST = (0, -1)

        table = {
            "|": [NORTH, SOUTH],
            "-": [EAST, WEST],
            "L": [NORTH, EAST],
            "J": [NORTH, WEST],
            "7": [SOUTH, WEST],
            "F": [SOUTH, EAST],
        }
        # find starting point first
        start = None
        for r in range(rows):
            for c in range(cols):
                if self.lines[r][c] == "S":
                    start = (r, c)

        adj = {}
        adj[start] = []
        ic(start)
        for r in range(rows):
            for c in range(cols):
                ch = self.lines[r][c]
                if ch == ".":
                    continue
                if ch == "S":
                    # we alrdy set start
                    continue
                first, second = table[ch]
                # make connections
                chd1 = (r + first[0], c + first[1])
                chd2 = (r + second[0], c + second[1])
                adj[(r, c)] = [chd1, chd2]

                if chd1 == start:
                    adj[start].append((r, c))
                if chd2 == start:
                    adj[start].append((r, c))

        ic(adj[start])

        # now itr
        # bfs the graph and find furthest point

        main_adj = {}
        Q = [(start, 0)]
        vis = set()
        furthest = 0
        while len(Q):
            curr, dist = Q.pop(0)
            ic(curr, dist)
            assert curr
            if curr in vis:
                continue
            vis.add(curr)
            furthest = max(furthest, dist)
            r, c = curr

            neighbors = adj[curr]
            main_adj[curr] = neighbors

            for neighbor in neighbors:
                if neighbor not in vis:
                    Q.append((neighbor, dist + 1))  # type: ignore
        # ic(dist)
        # ic(dist // 2)
        # print(dist, dist // 2)
        # return to renderer
        return main_adj


def export_to_render(fn: str):
    ic.disable()
    # if len(sys.argv) > 2 and sys.argv[2] == "-d":
    #     ic.disable()
    # else:
    #     ic.configureOutput(includeContext=True)
    soln = Soln(fn)
    adj = soln.solve()
    return adj


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
