#! /home/jstitt/repos/avent-of-coe-2023/.venv/bin/python3
# Advent of Code 2023 - Day 20 pt2 and 1 sorta

"""

THIS CODE IS A MESS BECAUSE I FORGOT TO SPLIT pt 1 and pt 2.
ALSO, I SORTA JUST USED https://www.calculatorsoup.com/calculators/math/lcm.php
AND THE CODE IN THIS FILE WAS REALLY JUST USED AS A REPL SO I CAN FIND CYCLES AND
DO MATH. THIS CODE DEF DOESNT RUN LOL
"""
import sys
import itertools
import functools
import re
from icecream import ic
from collections import defaultdict

LOW, HIGH = 0, 1

Q = []

COUNT = 0


class RX:
    def __init__(self):
        ...

    def receive_signal(self, _from: str, signal: int):
        if signal == LOW:
            print("DONE")
            print(COUNT)
            exit(0)


class Output:
    def __init__(self):
        self.lows = 0
        self.highs = 0

    def receive_signal(self, _from: str, signal: int):
        # print(f"{_from} -{'high' if signal==HIGH else 'low'}-> output")
        self.lows += 1 if signal == LOW else 0
        self.highs += 1 if signal == HIGH else 0


class FlipFlop:
    def __init__(self, name, connections, lookup):
        self.name = name
        self.on = False
        self.connections: list[str] = connections
        self.lookup = lookup

    def receive_signal(self, _from: str, signal: int):
        # print(f"{_from} -{'high' if signal==HIGH else 'low'}-> {self.name}")
        assert signal in (LOW, HIGH), f"bad signal: {signal}"
        if signal == LOW:
            mem = self.on
            self.on = not self.on
            for conn in self.connections:
                obj = self.lookup[conn]
                # obj.receive_signal(self.name, HIGH if not mem else LOW)
                nc = self.name[::]
                if not mem:
                    Q.append([nc, conn, HIGH])
                else:
                    Q.append([nc, conn, LOW])

        elif signal == HIGH:
            return


class Conjunction:
    def __init__(self, name, connections, lookup):
        self.name = name
        self.connections: list[str] = connections
        self.memory: defaultdict[str, int] = defaultdict(lambda: int(LOW))
        self.lookup = lookup
        self.refcnt = 0

    def receive_signal(self, _from: str, signal: int):
        # print(f"{_from} -{'high' if signal==HIGH else 'low'}-> {self.name}")
        self.memory[_from] = signal
        # print(f"{self.name} | {self.memory}")
        to_send = HIGH
        if self.refcnt == len(self.memory.values()) and all(
            [x == HIGH for x in self.memory.values()]
        ):
            to_send = LOW

        for conn in self.connections:
            obj = self.lookup[conn]
            nc = self.name[::]
            Q.append([nc, conn, to_send])
            # obj.receive_signal(self.name, to_send)


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]
            self.rows = len(self.lines)
            self.cols = len(self.lines[0])

    def solve(self):
        broadcasts = []
        lookup: dict[str, FlipFlop | Conjunction | Output] = {"output": Output()}
        num_button_presses = 1000
        lows, highs = 0, 0

        for line in self.lines:
            items = line.split("-> ")[-1].split(",")
            items = [x.strip() for x in items]
            if "broadcaster" in line:
                broadcasts.extend(items)
                continue
            _type = line[0]
            line = line[1:]
            name = line[: line.index(" ")].strip()
            # ic(_type, name)
            if _type == "%":
                ff = FlipFlop(name, items, lookup)
                lookup[name] = ff
            elif _type == "&":
                conj = Conjunction(name, items, lookup)
                lookup[name] = conj
            # ic(lookup)

        to_add = {}
        for name, obj in lookup.items():
            if name == "output":
                continue
            for obj_name in obj.connections:  # type: ignore
                try:
                    other = lookup[obj_name]
                except KeyError:
                    to_add[obj_name] = RX()
                else:
                    if isinstance(other, Conjunction):
                        other.refcnt += 1
        lookup.update(to_add)
        global COUNT
        # lookup["a"].receive_signal("test", LOW)
        # ic(lookup["a"].on)
        state_same_idx = None

        for i in range(num_button_presses * 10000):
            lows += 1
            for item_name in broadcasts:
                lows += 1
                obj = lookup[item_name]
                obj.receive_signal("broadcast", LOW)

            while len(Q):
                who, where, sig = Q.pop(0)
                # quests = ["xl", "ln", "xp", "gp"]
                # shared = []
                # if who == "gp" and where == "df" and sig == HIGH:
                #     print(f"gp done at {i=}")
                #     exit(0)
                # xl = 4050
                # ln = 4020
                # xp = 4056
                # gp = 3832
                # LCM = 87,864,215,400
                # try increasing by one each then LCM is:
                # 253302889093151 YEP WORKED LOL
                # https://www.calculatorsoup.com/calculators/math/lcm.php
                # too low!
                # for quest in quests:
                #     if who == quest and where == "df" and sig == HIGH:
                #         shared.append(who)

                # print(f"WHO: {shared}: {i = }")

                obj = lookup[where]
                lows += 1 if sig == LOW else 0
                COUNT = lows
                highs += 1 if sig == HIGH else 0
                obj.receive_signal(who, sig)
            # end of button press, check state
            # all flip-flops are OFF and all conjunctions have all LOW memory
            # is_og = True
            # for name, obj in lookup.items():
            #     if isinstance(obj, FlipFlop):
            #         if obj.on == True:
            #             is_og = False
            #             break
            #     elif isinstance(obj, Conjunction):
            #         for fro, sig in obj.memory.items():
            #             if sig != LOW:
            #                 is_og = False
            #                 break

            # if is_og:
            #     print(
            #         f"REACHED SAME OG STATE AT BUTTON PUSH: {i} with cycle count {i+1}",
            #     )
            #     exit(0)

        # ic(Q)

        # for name, obj in lookup.items():
        #     lows += obj.lows
        #     highs += obj.highs

        ic(lows, highs)
        print(lows * highs)


# fmt: off
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    else: ic.configureOutput(includeContext=True)
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
