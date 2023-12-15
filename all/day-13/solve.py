#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 13
import sys
import itertools
import functools
import re
from icecream import ic
from collections import defaultdict, Counter


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]
            self.rows = len(self.lines)
            self.cols = len(self.lines[0])

    def is_reflection(self, row):
        n = len(row)
        revs = []
        for i in range(1, n):
            left = row[:i]
            right = row[i:]
            # ic(left, right)
            rev_and_shrink = left[::-1][: len(right)]
            # ic(rev_and_shrink)
            if rev_and_shrink == right and len(right):
                ic(left, right, rev_and_shrink, row[:i] + "|" + row[i:], i)
                revs.append(i)

        return revs

    # NOTE: small hand modified
    def solve(self):
        # check
        # chunk = [
        #     "#...#.##.",
        #     "#...#.##.",
        #     "..#.#....",
        #     "...#.....",
        #     ".##.##..#",
        #     "##...####",
        #     "#.#.#####",
        #     "#.##.#...",
        #     ".###.....",
        #     "#.#.#####",
        #     "###.##..#",
        #     ".#..##..#",
        #     ".#....##.",
        # ]
        # transpose = [
        #     "....###..###.",
        #     "##...##..#..#",
        #     "##...##..#..#",
        #     "....####.###.",
        #     "###.#.#..###.",
        #     "...#...##....",
        #     "..#.#.#####..",
        #     "....##..#.###",
        #     "##...###.##..",
        # ]
        # test_set = set()
        # for idx, line in enumerate(chunk):
        #     ic(line)
        #     result = self.is_reflection(line)
        #     ic(result)
        #     if not len(result):
        #         test_set.clear()
        #         break
        #     if not len(test_set) and idx == 0:
        #         test_set |= set(result)
        #     else:
        #         ic("before", test_set)
        #         test_set &= set(result)
        #         ic("after", test_set)

        # exit(0)
        # ans = self.is_reflection("#.##.#...")
        # print(ans)
        # exit(0)
        revs = []
        so_far = []
        chunks = []
        so_far = []
        for line in self.lines:
            # ic(line)
            if line == "" or line == "x":
                chunks.append(so_far[::])
                so_far.clear()
                continue

            so_far.append(line)

        # ic(chunks)
        # exit(0)
        total = 0
        for chunk in chunks:
            # transpose = [
            #     "".join([chunk[j][i] for j in range(len(chunk))])
            #     for i in range(len(chunk[0]))
            # ]
            transpose = [
                "".join([chunk[j][i] for j in range(len(chunk))])
                for i in range(len(chunk[0]) - 1, -1, -1)
            ]
            # transpose = list(zip(*chunk))
            # ic(transpose)
            # transpose = ["".join(x) for x in transpose]
            # ic(transpose)

            v_com = set()
            h_com = set()

            most_common_v = Counter()
            most_common_h = Counter()
            for idx, line in enumerate(chunk):
                rs = self.is_reflection(line)
                for r in rs:
                    most_common_v[r] += 1
                ic("original: ", rs, line)
                if not len(rs):
                    v_com.clear()
                    break
                if not len(v_com) and idx == 0:
                    v_com |= set(rs)
                else:
                    ic("before", v_com)
                    v_com &= set(rs)
                    ic("after", v_com)

            for idx, line in enumerate(transpose):
                rs = self.is_reflection(line)
                for r in rs:
                    most_common_h[r] += 1
                ic("transpose: ", rs, line)
                if not len(rs):
                    h_com.clear()
                    break
                ic(rs)  # 8402 too low
                if not len(h_com) and idx == 0:
                    h_com |= set(rs)
                else:
                    ic("before", h_com)
                    h_com &= set(rs)
                    ic("after", h_com)
            ic(chunk)
            ic(transpose)
            ic(h_com, v_com)
            ic(most_common_h, most_common_h.most_common(1), len(most_common_h))
            if len(h_com) and len(v_com):
                assert False, "uh oh"
            if not len(h_com) and not len(v_com):
                try:
                    h_more = (
                        most_common_h.most_common(1)[0][1]
                        > most_common_v.most_common(1)[0][1]
                    )
                except:
                    if len(most_common_v):
                        v_com.add(most_common_v.most_common(1)[0][0])
                else:
                    if h_more and len(most_common_h):
                        h_com.add(most_common_h.most_common(1)[0][0])

            #     assert False, "bad again"
            if len(v_com):
                total += max(v_com)
                ...
            elif len(h_com):
                total += max(h_com) * 100
                ...
            # ic(chunk)
            # ic(transpose)
            # ic(v_com)
            # ic(h_com)
            # # exit(0)

        print(total)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
