import math
#   Number of paths taken


def f(i):
    return math.factorial(i)


def _f(i):
    p = 1
    for n in range(2,i+1):
        p = p * n
    return p


def main():
    print(f(100))
    print(_f(100))
#    print(f(2*20)/((f(20)**2)))
