def counted(x, y):
    return ((x**2 + x) * (y**2 + y))/4


def main():
    testfor = 2000000
    error = testfor

    x = 1
    y = 1
    while counted(x, y) <= testfor:
        x += 1

    while x >= y:
        if abs(counted(x, y) - testfor) < error:
            error = abs(counted(x, y) - testfor)
            area = x*y
        if counted(x, y) > testfor:
            x -= 1
        else:
            y += 1

    print(x, y, counted(x, y), area)


if __name__ == "__main__":
    main()
