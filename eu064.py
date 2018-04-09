def period(r):
    p = int(r**.5)
    if p * p == r:
        return 0
    q = 1
    remainders = {}
    pos = 0
    while True:
        pos = pos + 1
        q = (r - (p * p)) / q
        floor = int(((r**.5) + p) / q)
        p = -1 * (p - (floor * q))
        if (p, q) in remainders:
            return pos - remainders[p, q]
        remainders[p, q] = pos


def main():
    # print(period(23))
    print(sum(period(i) % 2 for i in range(2, 10001)))

