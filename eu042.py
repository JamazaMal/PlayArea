alp = ['"'] + list(map(chr, range(ord('A'), ord('Z')+1)))


def namScore(s):
    return sum(list(map(alp.index, [cc for cc in s])))


def _main():
    print(namScore("ZZZ"))


def main():
    f = open('042.txt', 'r')
    ret = 0
    nams = f.read().split(',')
    for n in nams:
        i = namScore(n)
        j = ((8*i)+1)**0.5
        if j == int(j):
            ret = ret + 1
    print(ret)
