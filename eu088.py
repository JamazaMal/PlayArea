
def fact(_i):
    ret = [_i]
    for i in range(2, _i):
        if _i % i == 0:
            ret.append([_i/i]+[fact(i)])
    return(ret)


def main():
    for x in fact(32):
        print(x)


if __name__ == '__main__':
    main()
