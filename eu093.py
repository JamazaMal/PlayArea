import itertools as iter


def evaluate(ss):
    try:
        k = eval(ss)
        if k < 0 or k % 1 != 0:
            return 0
        return int(k)
    except:
        return 0


def allnums(nums):
    ret = []
    for num in iter.permutations(nums):
        for i in iter.combinations_with_replacement(['+','-','*','/'],3):
            for sig in iter.permutations(i):
                ret.append(evaluate('{}{}{}{}{}{}{}'.format(num[0], sig[0], num[1], sig[1], num[2], sig[2], num[3])))
                ret.append(evaluate('{}{}({}{}{}){}{}'.format(num[0], sig[0], num[1], sig[1], num[2], sig[2], num[3])))
                ret.append(evaluate('{}{}{}{}({}{}{})'.format(num[0], sig[0], num[1], sig[1], num[2], sig[2], num[3])))
                ret.append(evaluate('({}{}{}){}({}{}{})'.format(num[0], sig[0], num[1], sig[1], num[2], sig[2], num[3])))
                ret.append(evaluate('{}{}({}{}{}{}{})'.format(num[0], sig[0], num[1], sig[1], num[2], sig[2], num[3])))

    return(sorted(set(ret)))



def _main():
    j = allnums([1,2,5,8])
    print(j)


def main():
    best = 0
    for i in iter.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4):
        j = allnums(i)
        c = 0
        for d, n in enumerate(j):
            if d == n == c:
                c += 1

        if c > best:
            best = c
            print(c, i, j)

        pass

