import time
import math
import decimal
import multiprocessing

mx = 1000000000


def areaint(a, b):
    h = decimal.Decimal(math.sqrt((a**2) - ((b/2)**2)), decimal.Context(prec=60))
    # h = ((a**2) - ((b/2)**2)) ** (1/2)
    return h % 1 == 0


def runit(i):
    res = 0
    c = 0
    if i == "+":
        for n in range(3, mx//2, 2):
            if n > c:
                if areaint(n, n+1):
                    print("++", res, n, n+1, (n*2) + (n+1))
                    res += (n*2) + (n+1)
                    c = n * 12
                    if c > mx:
                        break
    else:
        for n in range(3, mx//2, 2):
            if n > c:
                if areaint(n, n-1):
                    print("--", res, n, n-1, (n*2) + (n-1))
                    res += (n*2) + (n-1)
                    c = n * 12
                    if c > mx:
                        break
    return res


def main():
    pool = multiprocessing.Pool()
    print((pool.map(runit, ("+", "-"))))


if __name__ == '__main__':
    st = time.time()
    main()
    print("Duration : {} seconds.".format(time.time()-st))

