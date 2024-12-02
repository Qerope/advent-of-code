from aoc import read

pairs = [tuple(map(int, l.split())) for l in read(2024, 1).splitlines()]
left = sorted(a for a, _ in pairs)
right = sorted(b for _, b in pairs)
print(sum(abs(a - b) for a, b in zip(left, right)))
