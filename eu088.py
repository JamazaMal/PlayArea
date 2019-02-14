import itertools as it


def prod(_i):
    ret = 1
    for i in _i:
        ret = ret * i
    return ret


def k(_i):
    p = prod(_i)
    l = p - sum(_i)
    return [i for i in it.chain([1] * l, _i)], l+len(_i), p


def main():
    print(k([2, 2, 2]))


if __name__ == "__main__":
    main()
