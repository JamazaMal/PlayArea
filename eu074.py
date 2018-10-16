import math
df = [math.factorial(i) for i in range(10)]
fnd = [False] * 3000000


def digFac(i):
    z = 0
    for s in str(i):
        z = z + df[int(s)]
    return z


def dfloop(i, n):
    ret = n
    if n <= 60 and not(fnd[i]):
        fnd[i] = True
        ret = dfloop(digFac(i), n+1)

    fnd[i] = False
    return ret


def main():
    cc = 0
    for i in range(1000000):
        n = dfloop(i, 0)
        if n == 60:
            cc = cc + 1

    print(cc)
