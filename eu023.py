from functools import reduce


def sod(i):
    if i < 2:
        return i
    return reduce(lambda x, y: x+y, list(filter(lambda x: i % x == 0, range(1, i))))


def main():
    sods = list(map(sod, range(0, 28123)))
    print(sods)
