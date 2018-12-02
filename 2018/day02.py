from collections import Counter

from aoc import read

ids = read(2018, 2).split()
two = three = 0
for i in ids:
    counts = set(Counter(i).values())
    two += 2 in counts
    three += 3 in counts
print(two * three)

for a in ids:
    for b in ids:
        diff = [i for i in range(len(a)) if a[i] != b[i]]
        if len(diff) == 1:
            print(a[:diff[0]] + a[diff[0] + 1:])
            raise SystemExit
