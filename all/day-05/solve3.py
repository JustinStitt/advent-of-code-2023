#! /home/jstitt/repos/advent-of-code-2023/.venv/bin/python3
# Advent of Code 2023 - Day 5 pt 2 attempt 2 crazy idea
import sys
import itertools
import functools
import re
from icecream import ic
from collections import defaultdict
from random import randint


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

        ros = [
            range(int(x), int(x) + int(y)) for (x, y) in zip(seeds[::2], seeds[1::2])
        ]

        # fmt: off
        def go(seed):
            best = 10**18
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
            return best
        """
        logs:
            best ros defaultdict(<function Soln.solve.<locals>.<lambda> at 0x7f90e1c66660>, {2: 271557, 8: 78363, 4: 83238, 9: 14600, 7: 17839, 5: 32525, 3: 31722, 1: 13936, 0: 9279, 6: 2307})
            best ros defaultdict(<function Soln.solve.<locals>.<lambda> at 0x7f12fbf52660>, {5: 32518, 2: 271365, 0: 9116, 8: 78400, 4: 82967, 3: 31783, 9: 14959, 7: 17629, 1: 13890, 6: 2274})

            best ros [2088, 9]
            best ros [1720, 9]
            best ros [673, 9]
            best ros [15891, 9]

            best ro: 3107544690 59359615
        """
        # small = 10**18
        # for seed in seeds:
        #     result = go (seed)
        #     small = min(small, result)
        # print(small)
        # bro = range(3107544690, 3107544690+59359615)
        # small = 10**18
        # for seed in bro:
        #     r = go(seed)
        #     small=min(small, r)
        # print(small)
        rng = range(3267750502-10_000, 3267750502+1_000_000)
        smol = 10**18
        for i in rng:
            r = go(i)
            smol=min(smol, r)
        print('smol: ', smol)
        exit()

        # simulate
        # 3213715789 312116873 = 3525832662
        smol, big = 0, 4_000_000_000
        big = 3525832662 + 1
        for _ in range(5):
            min_result = [10**18, None, None]
            for _ in range(1_000_000):
                random_num = randint(smol, big)
                # what ro is this result from
                its_in = None
                for idx, ro in enumerate(ros):
                    if random_num in ro:
                        its_in = idx
                        break
                if its_in:
                    result = go(random_num)
                    if result < min_result[0]:
                        min_result[0] = result
                        min_result[1] = idx
                        min_result[2] = random_num

            print('best ros', min_result, flush=True)

        """
        best ros [31168656, 8]
        best ros [31165700, 8]
        best ros [31164980, 8]
        best ros [31161937, 8]
        best ros [31164410, 8]
        best ros [31162925, 8, 3267750502]
        best ros [31166662, 8, 3267754239]
        best ros [31165487, 8, 3267753064]
        best ros [31166246, 8, 3267753823]
        best ros [31168168, 8, 3267755745]
        best ros [31165170, 8, 3267752747]
        """


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
