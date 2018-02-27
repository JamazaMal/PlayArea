def r(a, n):
    return ((a*a) + ((n*n) / 2)-(n*a)) / (n-a)


def main():
    t = 0
    for n in range(2, 1001, 2):
        c = 0
        for i in range(1, (n//4)+1):
            k = r(i, n)
            if k == int(k):
                c = c + 1
        if c > t:
            print("p={} has {} solutions".format(n, c))
            t = c

