from aoc import read


def captcha(s, step):
    return sum(int(c) for i, c in enumerate(s) if c == s[(i + step) % len(s)])


if __name__ == '__main__':
    s = read(2017, 1)
    print(captcha(s, 1))
