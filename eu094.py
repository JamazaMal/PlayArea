import math
import decimal


def _areaInt(a, b):
    h = decimal.Decimal(math.sqrt((a**2) - ((b/2)**2)), decimal.Context(prec = 60))
    print(h)
    h = h - int(h)
    print(h)
    a = decimal.Decimal(h * b / 2, decimal.Context(prec = 60))
    print(a)
    return a == int(a)


def areaInt(a, b):
    h = decimal.Decimal(math.sqrt((a**2) - ((b/2)**2)), decimal.Context(prec = 60))
    return (h) == int(h)


def _main():
    a = 112803841
    b = 112803841-1

    print(areaInt(a, b))


def main():
    res = 0
    mx = 1000000000
    c = 0
    for n in range(3, mx//3, 2):
        if n > c:
            if areaInt(n, n-1):
                print(n, n-1, (n*2) + (n-1))
                res += (n*2) + (n-1)
                c = n * 12
                if c > mx:
                    break
    c = 0
    for n in range(3, mx//3, 2):
        if n > c:
            if areaInt(n, n+1):
                print(n, n+1, (n*2) + (n+1))
                res += (n*2) + (n+1)
                c = n * 12
                if c > mx:
                    break
    print(res)
