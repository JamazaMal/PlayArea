alp = ['"'] + list(map(chr, range(ord('A'), ord('Z')+1)))


def namScore(s):
    return sum(list(map(alp.index, [cc for cc in s])))


def main():
    f = open('022.txt', 'r')
    nams = sorted(f.readline().split(','))
    vals = map(namScore, nams)
    c = 0
    for i, v in enumerate(vals):
        c = c + ((i+1)*v)
    print(c)