import functools

def _f(i):
    p = 1
    for n in range(2, i+1):
        p = p * n
    return p


def f(i):
    return functools.reduce(lambda x, y: x + y, [int(c) for c in str(functools.reduce(lambda x, y: x * y, range(1, i)))])


def main():
    print(f(100))
    s = [int(c) for c in str(_f(100))]
    print(sum(s))
