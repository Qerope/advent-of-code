from math import prod

from aoc import read

grid = read(2020, 3).splitlines()


def trees(dx, dy):
    return sum(grid[y][(y // dy * dx) % len(grid[0])] == '#' for y in range(0, len(grid), dy))


print(trees(3, 1))
