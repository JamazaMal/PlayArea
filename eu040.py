import math

def main():
    p = 0
    r = 1
    for i in range(1, 1000001):
        for c in str(i):
            p = p + 1
            ll = math.log10(p)
            if ll == int(ll):
                r = r * int(c)
        if p >= 1000000:
            break
    print(r)
