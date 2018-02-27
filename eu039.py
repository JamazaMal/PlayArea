def r(a, n):
    return ((a*a)+((n*n)/2)-(n*a))/(n-a)


def main():
    t = 0
    for n in range(2, 1001, 2):
        c = 0
        for i in range(1, n // 4):
            k = r(i, n)
            if k == int(k):
                c = c + 1
        if c > t:
            print("p={} has {} solutions".format(n, c))
            t = c


def _main():
    t = 0
    for n in range(2, 1001, 2):
        c = 0
        for i in range(1, n//4):
            for j in range(i, n//2):
                k = n-i-j
                if k < 0:
                    break
                if (i**2 + j**2) ** 0.5 == k:
                    c = c + 1
        if c > t:
            print("p={} has {} solutions".format(n,c))
            t = c

