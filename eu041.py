from math import log10


def primes(n):
    mx = 0
    prs = [True] * (n+1)
    prs[0], prs[1] = [False] * 2
    for i, v in enumerate(prs):
        if v:
            ss = set(str(c) for c in range(1, int(log10(i)+1)+1))
            if set(str(i)) == ss and len(str(i)) == len(ss):
                mx = i
            prs[i*2::i] = [False] * ((n//i)-1)
    return mx


def main():
    print(primes(7654322))