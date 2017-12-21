from aoc import read


def run(offsets, part2=False):
    jumps = list(offsets)
    pc = steps = 0
    while 0 <= pc < len(jumps):
        j = jumps[pc]
        jumps[pc] += -1 if part2 and j >= 3 else 1
        pc += j
        steps += 1
    return steps


if __name__ == '__main__':
    data = [int(x) for x in read(2017, 5).split()]
    print(run(data))
    print(run(data, True))
