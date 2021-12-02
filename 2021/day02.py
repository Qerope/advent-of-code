from aoc import read

cmds = [(a, int(b)) for a, b in (l.split() for l in read(2021, 2).splitlines())]
x = depth = 0
for c, n in cmds:
    if c == 'forward':
        x += n
    elif c == 'down':
        depth += n
    else:
        depth -= n
print(x * depth)

x = depth = aim = 0
for c, n in cmds:
    if c == 'forward':
        x += n
        depth += aim * n
    elif c == 'down':
        aim += n
    else:
        aim -= n
print(x * depth)
