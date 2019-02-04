import itertools

pairs = []
singles = []


def popPair(i, j):
    global pairs
    global singles
    if i not in singles:
        singles += i
    if j not in singles:
        singles += j
    if (i, j) not in pairs:
        pairs += [[i, j]]


def popAll(s):
    for i in range(len(s)-2):
        for j in range(i+1, len(s)-1):
            popPair(s[i], s[j])


with open('079.txt', 'r') as f:
    for l in f:
        popAll(l)


def checkPairs(cc):
    for p in pairs:
        fnd = False
        for i in range(len(cc)-1):
            for j in range(i+1, len(cc)):
                if cc[i] == p[0] and cc[j] == p[1]:
                    fnd = True
        if not fnd:
            return False
    return True


def main():
    for i in itertools.permutations(singles):
        if checkPairs(i):
            print(i)
            break


