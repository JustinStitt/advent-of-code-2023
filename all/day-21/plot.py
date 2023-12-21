import sys
import re
from icecream import ic
import matplotlib.pyplot as plt

lines = [line.strip() for line in sys.stdin.readlines()]

x = []
y = []
z = []
for line in lines:
    _x = re.findall(r"= \d+ <", line)[0][2:-2]
    ridx = len(line) - line[::-1].index(" ")
    _y = int(line[ridx:])
    _x = int(_x)
    # area = (_x + 1) ** 2
    # answer = _y
    # density = answer / area
    x.append(_x)
    y.append(_y)

plt.plot(x, y)
plt.show()

assert len(x) == len(y)
print(x)
print(y)
# for r in range(0, len(x), 10):
#     print(x[r], end=",")
# print()
# for r in range(0, len(y), 10):
#     print(y[r], end=",")
