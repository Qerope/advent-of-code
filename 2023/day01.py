from aoc import read

lines = read(2023, 1).splitlines()


def value(line):
    d = [c for c in line if c.isdigit()]
    return int(d[0] + d[-1])


print(sum(value(l) for l in lines))

WORDS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def digits(line):
    out = []
    for i, c in enumerate(line):
        if c.isdigit():
            out.append(c)
        for n, w in enumerate(WORDS, 1):
            if line.startswith(w, i):
                out.append(str(n))
    return out


print(sum(int(digits(l)[0] + digits(l)[-1]) for l in lines))
