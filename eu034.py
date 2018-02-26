def f(n):
    res = 0
    for c in str(n):
        r = 1
        for i in range(1, int(c)+1):
            r = r * i
        res = res + r
    return res


def main():
    s = 0
    for i in range (3,41000):
        if f(i) == i:
            s=s+i
            print ("{}-{}".format(i,i))
    print(s)