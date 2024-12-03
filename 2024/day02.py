from aoc import read

reports = [list(map(int, l.split())) for l in read(2024, 2).splitlines()]


def safe(r):
    d = [b - a for a, b in zip(r, r[1:])]
    return all(1 <= x <= 3 for x in d) or all(-3 <= x <= -1 for x in d)


print(sum(safe(r) for r in reports))
print(sum(safe(r) or any(safe(r[:i] + r[i + 1:]) for i in range(len(r))) for r in reports))
