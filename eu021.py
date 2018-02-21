import functools


def sod(i):
    return functools.reduce(lambda x, y: x+y, list(filter(lambda x: i % x == 0, range(1, i))))


def main():
    ll = [0, 0] + [sod(i) for i in range(2, 100)]
    print(ll)