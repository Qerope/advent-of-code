from aoc import read

lines = read(2023, 1).splitlines()


def value(line):
    d = [c for c in line if c.isdigit()]
    return int(d[0] + d[-1])


print(sum(value(l) for l in lines))
