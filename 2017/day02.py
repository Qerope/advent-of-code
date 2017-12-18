from aoc import read


def rows(text):
    return [[int(x) for x in line.split()] for line in text.splitlines()]


if __name__ == '__main__':
    r = rows(read(2017, 2))
    print(sum(max(x) - min(x) for x in r))
    total = 0
    for row in r:
        for a in row:
            for b in row:
                if a != b and a % b == 0:
                    total += a // b
    print(total)
