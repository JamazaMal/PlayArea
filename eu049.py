def getPrimes():
    mx = 10000
    ret = set()
    ps = [True]*(mx + 1)
    ps[0], ps[1] = [False] * 2

    for i, v in enumerate(ps):
        if v:
            if i > 1000:
                ret.add(i)
            ps[i*2::i] = [False] * ((mx//i)-1)

    return ret

def main():
    prm = getPrimes()
    for i in prm:
        s = set(str(i))
        for j in range(1112, (10000-i)//2, 2):
            if i + j in prm and i + j + j in prm:
                sj = set(str(i+j))
                if s ^ sj == set(): # if sets are same
                    sj = set(str(i + j + j))
                    if s ^ sj == set():
                        print(j, i, i+j, i+j+j)
