from aoc import read

moves = [(l[0], int(l[1:])) for l in read(2025, 1).splitlines()]
pos = 50
zeros = 0
for d, n in moves:
    pos = (pos + (n if d == 'R' else -n)) % 100
    zeros += pos == 0
print(zeros)
