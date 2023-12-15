#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 15 pt 2
import sys
import itertools
import functools
import re
from icecream import ic
from collections import defaultdict


def HASH(s: str):
    curr = 0
    for c in s:
        ascii = ord(c)
        curr += ascii
        curr *= 17
        curr %= 256
    return curr


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]
            self.rows = len(self.lines)
            self.cols = len(self.lines[0])

    def solve(self):
        seq = self.lines[0].split(",")
        boxes = []
        for _ in range(256):
            boxes.append(list())

        # ic(HASH("cm"), HASH("rn"), HASH("xx"))
        for item in seq:
            match = re.search(r"[a-z]+", item)
            assert match
            label = item[: match.end()]

            op = item[match.end()]
            ic(label, op)
            box_idx = HASH(label)
            if op == "=":
                focal_length = item[match.end() + 1]
                found = False
                for i in range(len(boxes[box_idx])):
                    _label, _focal = boxes[box_idx][i]
                    if _label == label:
                        boxes[box_idx][i][1] = focal_length
                        found = True
                        break
                if not found:
                    boxes[box_idx].append([label, focal_length])
            elif op == "-":
                ...
                for i in range(len(boxes[box_idx])):
                    if boxes[box_idx][i][0] == label:
                        boxes[box_idx][i][0] = None
                        break

            else:
                assert False, f"idk, sohuldnt be here tho xd {item}"

        # ic(boxes)
        total = 0
        for box_num in range(len(boxes)):
            box = boxes[box_num]
            box_num += 1
            non_none = 0
            for _label, _focal in box:
                if _label is None:
                    continue
                non_none += 1
                power = int(box_num) * int(non_none) * int(_focal)
                ic(power)
                total += power
        print(total)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
