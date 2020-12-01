from itertools import combinations
from math import prod

from aoc import read

nums = [int(x) for x in read(2020, 1).split()]
print(next(prod(c) for c in combinations(nums, 2) if sum(c) == 2020))
