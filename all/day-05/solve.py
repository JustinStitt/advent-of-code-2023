#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 5
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
        seeds = self.lines[0].split(" ")[1:]
        seed_to_soil = defaultdict(lambda: lambda x: x)
        soil_to_fert = defaultdict(lambda: lambda x: x)
        fert_to_water = defaultdict(lambda: lambda x: x)
        water_to_light = defaultdict(lambda: lambda x: x)
        light_to_temp = defaultdict(lambda: lambda x: x)
        temp_to_humid = defaultdict(lambda: lambda x: x)
        humid_to_location = defaultdict(lambda: lambda x: x)
        ic(seeds)
        idx = 2

        def closure(dr, sr):
            ic(dr, sr)
            return lambda x: abs(sr - x) + dr

        while idx < len(self.lines):
            line = self.lines[idx]
            if "map" in line:
                cm = None
                if "to-soil" in line:
                    cm = seed_to_soil
                elif "to-fert" in line:  # TODO rest of these
                    cm = soil_to_fert
                elif "to-water" in line:
                    cm = fert_to_water
                elif "to-light" in line:
                    cm = water_to_light
                elif "to-temp" in line:
                    cm = light_to_temp
                elif "to-humid" in line:
                    cm = temp_to_humid
                elif "to-loca" in line:
                    cm = humid_to_location
                assert cm is not None, "bad cm"
                idx += 1
                while idx < len(self.lines) and self.lines[idx] != "":
                    dr, sr, l = [int(x) for x in self.lines[idx].split(" ")]
                    # ic(abs(dr - 51) + sr)
                    cm[range(sr, sr + l)] = closure(dr, sr)
                    idx += 1
            else:
                idx += 1
        best = 10**18

        # fmt: off
        for seed in seeds:
            val = int(seed)
            for m in [seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_humid, humid_to_location]:
                ic(m)
                was_in = False
                for k, v in m.items():
                    if val in k:
                        was_in = True
                        ic(val, v(val))
                        val = v(val)
                        if m is humid_to_location:
                            best = min(val, best)
                        break
                if not was_in and m == humid_to_location:
                    best = min(val, best)
        print(best)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
