from aoc import read

ranges = [tuple(map(int, r.split('-'))) for r in read(2025, 2).split(',')]


def invalid(n):
    s = str(n)
    h = len(s) // 2
    return len(s) % 2 == 0 and s[:h] == s[h:]


print(sum(n for lo, hi in ranges for n in range(lo, hi + 1) if invalid(n)))


def invalid2(n):
    s = str(n)
    return any(len(s) % k == 0 and s[:k] * (len(s) // k) == s for k in range(1, len(s) // 2 + 1))


print(sum(n for lo, hi in ranges for n in range(lo, hi + 1) if invalid2(n)))
