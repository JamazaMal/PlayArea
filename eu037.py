ps = []

def primes(n):
    prs = [True] * (n+1)
    prs[0], prs[1] = [False] * 2
    for i, v in enumerate(prs):
        if v:
            prs[i*2::i] = [False] * ((n//i)-1)
    return prs


def canTrunc(n):
    s = ""
    if not ps[n]:
        return False
    for c in str(n):
        s = s + c
        if not ps[int(s)]:
            return False
    s = ""
    for c in str(n)[::-1]:
        s = c + s
        if not ps[int(s)]:
            return False
    return True


def main():
    global ps
    t = 0
    ps = primes(1000000)
    for i in range(11,1000000):
        if canTrunc(i):
            t = t + i
    print(t)