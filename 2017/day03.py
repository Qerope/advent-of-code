def distance(n):
    # ring k holds (2k-1)^2+1 .. (2k+1)^2
    if n == 1:
        return 0
    k = 0
    while (2 * k + 1) ** 2 < n:
        k += 1
    side = 2 * k
    offset = (n - (2 * k - 1) ** 2 - 1) % side
    return k + abs(offset - (k - 1))


if __name__ == '__main__':
    print(distance(368078))
