#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 17
import sys
import itertools
import functools
import re
from icecream import ic
from collections import defaultdict
from heapq import heapify, heappop, heappush

NORTH, EAST, SOUTH, WEST = (0, 1, 2, 3)


class State:
    def __init__(self, r, c, dir, cheat, st, path):
        self.r = r
        self.c = c
        self.dir = dir
        self.cheat = cheat
        self.straight_count = st
        self.path = path

    def __lt__(self, other) -> bool:
        if self.cheat < other.cheat:
            return True
        if self.cheat == other.cheat:
            return self.straight_count >= other.straight_count
        return False

    def __repr__(self):
        return f"{self.r=} {self.c=} {self.dir=} {self.cheat=} {self.straight_count=} {self.path=}"


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]
            self.rows = len(self.lines)
            self.cols = len(self.lines[0])
            self.m = self.lines

    def get_poss_moves(self, r, c, dir):
        deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        moves = []
        for dr, dc in deltas:
            if dir == EAST and dc == -1:
                continue
            if dir == WEST and dc == 1:
                continue

            if dir == NORTH and dr == 1:
                continue

            if dir == SOUTH and dr == -1:
                continue

            nr = r + dr
            nc = c + dc
            if nr < 0 or nr > self.rows - 1:
                continue
            if nc < 0 or nc > self.cols - 1:
                continue
            new_pos = (nr, nc)
            new_dir = None
            if dir == EAST:
                new_dir = (dir + dr) % 4
            elif dir == WEST:
                new_dir = (dir - dr) % 4
            # N E S W
            elif dir == NORTH:
                new_dir = (dir + dc) % 4
            elif dir == SOUTH:
                new_dir = (dir - dc) % 4
            heat = int(self.m[nr][nc])
            moves.append((new_pos, new_dir, dir == new_dir, heat))

        moves = sorted(moves, key=lambda x: x[3])
        return moves

    def solve(self):
        strt = (0, 0)
        end = (self.rows - 1, self.cols - 1)

        # ic(self.get_poss_moves(0, 0, dir=WEST))
        # exit(0)
        # pos, dir, cheat
        s = 0
        # too high 1124
        starting_state_e = State(strt[0], strt[1], EAST, 0, s, [])
        starting_state_s = State(strt[0], strt[1], SOUTH, 0, s, [])
        h = [starting_state_e, starting_state_s]
        heapify(h)

        vis = set()

        best = (None, 10**18)
        ic(self.m)
        while len(h):
            curr = heappop(h)
            _r = curr.r
            _c = curr.c
            _dir = curr.dir
            _cheat = curr.cheat
            _st = curr.straight_count

            if _st > 9:
                continue

            if (_r, _c, _dir, _st) in vis:
                continue

            if (_r, _c) == end and _st >= 3:
                ic("done")
                best = (curr, _cheat)
                break

            vis.add((_r, _c, _dir, _st))

            # neighbors
            poss_moves = self.get_poss_moves(_r, _c, _dir)
            assert len(poss_moves) <= 3, "bad move count"
            ic(poss_moves)

            for new_pos, new_dir, straight, heat in poss_moves:
                # ic((_r, _c), new_pos, _dir, new_dir)
                new_st = (_st + 1) if straight else s

                if not straight and _st < 3:
                    continue

                heappush(
                    h,
                    State(
                        new_pos[0],
                        new_pos[1],
                        new_dir,
                        _cheat + heat,
                        new_st,
                        curr.path[::]
                        + [(new_pos[0], new_pos[1], _cheat + heat, new_st)],
                    ),
                )
        ic(best)
        # too high
        last = int(self.m[end[0]][end[1]])
        # print(f"{best-self.m[end[0]][end]}")
        print(best[1] - last, flush=True)
        print(best[1], flush=True)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
