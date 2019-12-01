from aoc import read


def fuel(mass):
    return mass // 3 - 2


if __name__ == '__main__':
    masses = [int(x) for x in read(2019, 1).split()]
    print(sum(fuel(m) for m in masses))

    def total(mass):
        f = fuel(mass)
        return 0 if f <= 0 else f + total(f)

    print(sum(total(m) for m in masses))
