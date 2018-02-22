mx = 28125
sods = []


def spd(n):
    if n < 2:
        return n
    r = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            r = r + i + (n//i)
    if (n**0.5) == int(n**0.5):
        r = r - int(n**0.5)
    if r > n:
        return int(n)   # Is abundant
    return 0


def main():
    global sods
    j = 0
    ll = list(map(spd, range(2, mx)))
    ll.sort()
    for i in ll:
        if i < mx and i != j:
            j = i
            sods.append(i)

    ss = list(range(0,mx+1))
    for i in sods:
        if i >= mx:
            break
        for j in sods:
            if j + i > mx:
                break
            ss[i+j]=0

    print(sum(ss))
