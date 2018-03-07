import itertools


def is_match(i, j):
    return set(str(i))-set(str(j)) == set()


def main():
    for i in range(5, 10):
        for s in itertools.permutations("023456789", i):
            n = int("1" + "".join(s))
            if all(is_match(n, n*i) for i in range(6, 1, -1)):
                print(n)
                return
