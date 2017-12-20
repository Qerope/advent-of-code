from aoc import read

lines = [l.split() for l in read(2017, 4).splitlines()]
print(sum(len(set(w)) == len(w) for w in lines))
print(sum(len(set(''.join(sorted(x)) for x in w)) == len(w) for w in lines))
