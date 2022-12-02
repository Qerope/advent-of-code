from aoc import read

elves = sorted(sum(int(x) for x in block.split()) for block in read(2022, 1).split('\n\n'))
print(elves[-1])
print(sum(elves[-3:]))
