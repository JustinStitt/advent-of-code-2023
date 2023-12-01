import sys; print(sum(int(x[0]+x[-1]) for x in ''.join([c for line in sys.stdin.readlines() for c in line if c.isdigit() or c=='\n']).split('\n')[:-1]))
