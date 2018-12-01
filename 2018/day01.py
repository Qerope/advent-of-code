from aoc import read

changes = [int(x) for x in read(2018, 1).split()]
print(sum(changes))

seen = {0}
f = 0
while True:
    for c in changes:
        f += c
        if f in seen:
            print(f)
            raise SystemExit
        seen.add(f)
