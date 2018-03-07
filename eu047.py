
def main():
    mx = 150000
    z = 4

    f = [0]*(mx+z)
    c = 0

    for n in range(2,mx+z):
        if f[n] == z:
            c = c + 1
            if c == z:
                print(n-z+1)
                break
        else:
            c = 0
            if f[n] == 0:
                f[n::n] = [x + 1 for x in f[n::n]]


