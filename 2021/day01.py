from aoc import read

d = [int(x) for x in read(2021, 1).split()]
print(sum(b > a for a, b in zip(d, d[1:])))
