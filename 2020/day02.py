import re

from aoc import read

rows = [re.match(r'(\d+)-(\d+) (\w): (\w+)', l).groups() for l in read(2020, 2).splitlines()]
print(sum(int(lo) <= pw.count(c) <= int(hi) for lo, hi, c, pw in rows))
