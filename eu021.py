from functools import reduce
mx = 10000


def sod(i):
    return reduce(lambda x, y: x+y, list(filter(lambda x: i % x == 0, range(1, i))))


def main():
    ll = [-1, 0] + [sod(i) for i in range(2, mx)]
    c = 0
    for i, v in enumerate(ll):
        if v < mx:
            if v == ll[i] and i == ll[v] and v != i:
                c = c + i

    print(c)