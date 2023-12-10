#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 10 pt 2
import sys
import itertools
import functools
import re
from icecream import ic
from collections import defaultdict
import matplotlib.path


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
        Q = [(start, 0)]
        pts = []
        vis = set()
        furthest = 0
        main_adj = {}
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
        # print(pts)
        # GO FOLLOW PATH WITH DFS
        stk = [start]
        pts = []
        vis2 = set()
        while len(stk):
            curr = stk.pop()
            assert curr
            if curr in vis2:
                continue
            pts.append([curr[1], curr[0]])
            vis2.add(curr)

            for n in main_adj[curr]:
                if n in vis2: continue
                stk.append(n)
        # for key in main_adj:
        #     pts.append([key[1], key[0]])
        print(pts, len(pts), len(vis), len(vis2))
        # use pts with plt
        # 324 too low
        # 6967 too high
        # 5815 too high
        # fk should i just strat binary searching this?
        polygon = matplotlib.path.Path(pts)
        # https://matplotlib.org/stable/api/path_api.html oh fk
        total = 0
        for r in range(rows):
            for c in range(cols):
                if [c, r] not in pts and polygon.contains_point((c, r)): # dont count pts themselves right?
                    total += 1

        print('total: ', total)
# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
