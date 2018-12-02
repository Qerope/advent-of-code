from collections import Counter

from aoc import read

ids = read(2018, 2).split()
two = three = 0
for i in ids:
    counts = set(Counter(i).values())
    two += 2 in counts
    three += 3 in counts
print(two * three)
