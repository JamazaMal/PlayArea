import itertools
mx = 100000

def get_primes():
    ret = list()
    ps = [True]*(mx + 1)
    ps[0], ps[1] = [False] * 2

    for i, v in enumerate(ps):
        if v:
            ret.append(i)
            ps[i*2::i] = [False] * ((mx//i)-1)

    return ret


def get_positions(l,n):
    return set([k for k in itertools.permutations([True]*l + [False]*n) if k[l+n-1]])


def replace_digits(nset, nums):
    n = 0
    s = ""
    for b in nset:
        if b:
            s = s + nums[n]
            n = n + 1
        else:
            s = s + "x"
    return [int(s.replace("x", str(i))) for i in range(0,10) ]


def main():
    prm = get_primes()
    bst = 0
    for i in range(101, 10000, 2):
        for j in range(1, len(str(i))):
            p = get_positions(len(str(i)), j)
            for pp in p:
                t = sum(1 for k in replace_digits(pp, str(i)) if k in prm)
                if t > bst:
                    bst = t
                    print(t, replace_digits(pp, str(i)))
