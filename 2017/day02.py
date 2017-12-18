from aoc import read


def rows(text):
    return [[int(x) for x in line.split()] for line in text.splitlines()]


if __name__ == '__main__':
    r = rows(read(2017, 2))
    print(sum(max(x) - min(x) for x in r))
