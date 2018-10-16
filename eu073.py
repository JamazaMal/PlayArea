def f_seq(n, nf, df, nt, dt):
    adding = False
    n1, d1 = 0, 1
    n2, d2 = 1, n

    ret = []

    if nf == n1 and df == d1:
        adding = True
        ret.append([n1, d1])
        if nt == n1 and dt == d1:
            return ret

    if nf == n2 and df == d2:
        adding = True
        ret.append([n2, d2])
        if nt == n2 and dt == d2:
            return ret

    while not(n2 == 1 and d2 == 1):
        k = (n+d1)//d2
        n3 = (k * n2) - n1
        d3 = (k * d2) - d1
        if nf == n3 and df == d3:
            adding = True

        if adding:
            ret.append([n3, d3])

        if nt == n3 and dt == d3:
            return ret

        n1, d1 = n2, d2
        n2, d2 = n3, d3

    return ret


def main():
    n = f_seq(12000, 1, 3, 1, 2)
    print(len(n))
