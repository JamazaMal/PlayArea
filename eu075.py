from math import gcd


def pt(m, n):
    ra = (m * m) - (n * n)
    rb = 2 * m * n
    rc = (m * m) + (n * n)
    return [ra, rb, rc]


def main():

    mx = 1500000
    res = [0] * (mx+1)
    i = 0

    keepgoing = True
    while keepgoing:
        keepgoing = False
        i += 1
        j = i
        while True:
            j += 1
            if gcd(i, j) == 1 and (i+j) % 2 == 1:
                t = pt(j, i)
                if sum(t) > mx:
                    break
                k = 1
                while k*sum(t) <= mx:
                    res[k*sum(t)] += 1
                    k += 1
                keepgoing = True

    print(len([x for x in res if x == 1]))
