import re
from collections import defaultdict

from aoc import read

claims = [tuple(map(int, re.findall(r'\d+', l))) for l in read(2018, 3).splitlines()]
fabric = defaultdict(int)
for _, x, y, w, h in claims:
    for i in range(x, x + w):
        for j in range(y, y + h):
            fabric[(i, j)] += 1
print(sum(v > 1 for v in fabric.values()))
