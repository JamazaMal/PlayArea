pw = 5  # Which power to use
pows = [i**pw for i in range(0, 10)]


def main():
    t = 0
    for n in range(2,194980):
        p = sum(pows[int(i)] for i in str(n))
        if p == n:
            t = t + p
            print("{} - {}".format(p, n))
    print(t)