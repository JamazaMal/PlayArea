def cntr(hnd):
    h = {} # Dictionary
    for i in hnd:
        h[i[0]] = h.get(i[0], 0) + 1
    ret = [(h[i], '23456789TJQKA'.find(i)) for i in h]
    return sorted(ret, reverse=True)


def handScr(hnd):
    scr = list(zip(*cntr(hnd)))
    scr[0] = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (), (), (3, 2), (4, 1)].index(scr[0])

    # Check for straight, if (1, 1, 1, 1, 1) - No sets
    if scr[0] == 0:
        scr[0] = 4
        if scr[1] != [11, 0, 1, 2, 3]:  # Ace low straight
            for i in range(4):
                if scr[1][i] != scr[1][i+1]+1:
                    scr[0] = 0

    # Check Flush
    if (len(set(i[1] for i in hnd))) == 1: # Just one suit means flush
        scr[0] = scr[0] + 5

    return(scr)


def main():
    p1 = 0
    hands = (line.split() for line in open('054.txt'))
    for hnd in hands:
        if handScr(hnd[:5]) > handScr(hnd[5:]):
            p1 = p1 + 1
    print(p1)

