import itertools
prms = list()
min = 10000000000


def isprime(n):
    if n in prms:
        return True
    return all(n%i for i in range(2,int(n**.5)+1))


def primes(n):
    ret = list()
    prs = [True] * (n+1)
    prs[0], prs[1] = [False] * 2
    for i, v in enumerate(prs):
        if v:
            ret = ret + [i]
            prs[i*2::i] = [False] * ((n//i)-1)
    return ret


def testlist(l):
    for i in range(len(l)-1):
        if not isprime(int(str(l[i]) + str(l[len(l)-1]))):
            return False
        if not isprime(int(str(l[len(l)-1]) + str(l[i]))):
            return False
    return True


def dowork(l):
    global min
    if len(l) == 5:
        min = sum(l)
        print(l, sum(l))
        return

    for i in range(prms.index(l[len(l)-1])+1, len(prms)):
        if sum(l + [prms[i]]) < min:
            if testlist(l + [prms[i]]):
                dowork(l + [prms[i]])

    return


def main():
    global prms
    prms = primes(10000)

    for i in prms:
        dowork([i])


