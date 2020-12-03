import sys


def read(year, day):
    with open('inputs/%d/day%02d.txt' % (year, day)) as f:
        return f.read().strip()


def lines(year, day):
    return read(year, day).splitlines()
