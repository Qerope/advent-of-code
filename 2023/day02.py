import re

from aoc import read

limits = {'red': 12, 'green': 13, 'blue': 14}
games = {}
for line in read(2023, 2).splitlines():
    gid, rest = line.split(': ')
    games[int(gid.split()[1])] = [(int(n), c) for n, c in re.findall(r'(\d+) (\w+)', rest)]
print(sum(g for g, cubes in games.items() if all(n <= limits[c] for n, c in cubes)))
