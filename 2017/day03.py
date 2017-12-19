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

def first_larger(limit):
    grid = {(0, 0): 1}
    x = y = 0
    dx, dy = 1, 0
    while True:
        x, y = x + dx, y + dy
        v = sum(grid.get((x + i, y + j), 0) for i in (-1, 0, 1) for j in (-1, 0, 1))
        if v > limit:
            return v
        grid[(x, y)] = v
        # turn left when the cell to the left is empty
        if (x - dy, y + dx) not in grid:
            dx, dy = -dy, dx


if __name__ == '__main__':
    print(first_larger(368078))
