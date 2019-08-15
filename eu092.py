mx = 10000001
fnd = [False] * (mx + 1)

def to89(x):
    n = x
    while n not in [1, 89]:
        if fnd[n]: return True
        r = n
        n = 0
        for i in str(r):
            n += int(i) ** 2
    return n == 89


def main():
    global fnd
    res = 0
    for i in range(1, mx):
        if to89(i):
            fnd[i] = True
            res += 1
    print(res)
