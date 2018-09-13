from math import gcd


def phi(_i):
    t = 1
    for j in range(2, _i):
        if gcd(_i, j) == 1:
            t = t + 1
    return t


def main():
    best = 0
    for i in range(10000):
        j = i/phi(i)
        if j > best:
            best = j
            print(i,j)


