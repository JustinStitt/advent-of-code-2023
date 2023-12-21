import sys
from icecream import ic


lines = [line.strip() for line in sys.stdin.readlines()]

n = 64
start_r = len(lines) % (n + 1)
ic(start_r)
# for line in lines:

cnt = 0
total = 0
dec = False
for i in range(n * 2 + 1):
    cnt += 1 if not dec else -1
    r = start_r + i
    slice = lines[r][(n + 1 - i) : (n + 1 + i + 1)]
    num_rock_on_even = sum([1 for i, x in enumerate(slice) if i % 2 == 0 and x == "#"])
    total += cnt - num_rock_on_even
    if i >= (n * 2 + 1) // 2 and not dec:
        dec = True
    predict = cnt - num_rock_on_even
    actual = slice.count("O")
    ic(r)
    ic(slice)
    ic(cnt, dec)
    ic(num_rock_on_even)
    ic(predict, actual)
    assert predict == actual, "bad predict"

print(total)
