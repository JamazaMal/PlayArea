from math import factorial


def C(n, r):
    return factorial(n)/(factorial(r) * factorial(n-r))


def main():
    tot = 0
    for i in range(23, 101):
        tot = tot + sum(C(i, j) > 1000000 for j in range(1, i+1))

    print(tot)