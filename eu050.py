mx = 1000000

def getPrimes():
    ret = list()
    ps = [True]*(mx + 1)
    ps[0], ps[1] = [False] * 2

    for i, v in enumerate(ps):
        if v:
            ret.append(i)
            ps[i*2::i] = [False] * ((mx//i)-1)

    return ret

def main():
    prm = getPrimes()
    bst = 1
    btt = 0
    for i in range(len(prm)//10000):
        for j in range(i+bst, len(prm)):
            t = sum(prm[k] for k in range(i, j+1))
            if t > mx:
                break
            if t in prm:
                if j-i+1 > bst:
                    btt = t
                    bst = j-i+1
    print(btt)
