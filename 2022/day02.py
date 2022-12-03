from aoc import read

rounds = [l.split() for l in read(2022, 2).splitlines()]
# A/X rock, B/Y paper, C/Z scissors
score = 0
for a, b in rounds:
    o, m = 'ABC'.index(a), 'XYZ'.index(b)
    score += m + 1 + 3 * ((m - o + 1) % 3)
print(score)

score = 0
for a, b in rounds:
    o, r = 'ABC'.index(a), 'XYZ'.index(b)
    m = (o + r - 1) % 3
    score += m + 1 + 3 * r
print(score)
