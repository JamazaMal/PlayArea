mk = 12000
res = [100000] * mk


def nextFact(pd, sm, fc, lf):
    k = pd - sm + fc
    if k < mk:
        if pd < res[k]:
            res[k] = pd
        for i in range(lf, mk//pd*2+1):
            nextFact(pd*i, sm+i, fc+1, i)


def main():
    nextFact(1, 1, 1, 2)
    print(sum(set(res[2:])))


if __name__ == "__main__":
    main()
