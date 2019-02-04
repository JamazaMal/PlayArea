import itertools as itr


def main():
    ls = list(i for i in range(1000000))
    x = sum(ls)



def _main():
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    for i in itr.combinations(ls, 6):
        j = tuple(x for x in ls if x not in i)
        t = 0
        for d1 in range(6):
            for d2 in range(6):
                t += i[d1] + j[d2]

        print(i, j, t)
