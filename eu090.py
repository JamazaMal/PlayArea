import itertools as iter


def cando(lc, rc):
    if not((0 in lc and 1 in rc) or (0 in rc and 1 in lc)): return False
    if not((0 in lc and 4 in rc) or (0 in rc and 4 in lc)): return False
    if not((0 in lc and 6 in rc) or (0 in rc and 6 in lc)): return False
    if not((1 in lc and 6 in rc) or (1 in rc and 6 in lc)): return False
    if not((1 in lc and 8 in rc) or (1 in rc and 8 in lc)): return False
    if not((2 in lc and 5 in rc) or (2 in rc and 5 in lc)): return False
    if not((3 in lc and 6 in rc) or (3 in rc and 6 in lc)): return False
    if not((4 in lc and 6 in rc) or (4 in rc and 6 in lc)): return False
    return True


def main():
    res = 0
    t = 0
    for i in iter.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 6], 6):
        for j in iter.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 6], 6):
            if cando(i, j):
                res += 1
    print(res/2)
