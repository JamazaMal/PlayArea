import itertools


def main():

    iref = [0, 1, 2, 3, 4, 0]
    for l in itertools.permutations(range(1, 11)):
        ol = l[0:5:]
        il = l[5:11:]
        sum = [0, 0, 0, 0, 0]
        sout = ""

        for c, o in enumerate(ol):
            sum[c] = o + il[iref[c]] + il[iref[c + 1]]
            sout = "{}{}{}{}".format(sout, o, il[iref[c]], il[iref[c + 1]])

        if sum[0] == sum[1] == sum[2] == sum[3] == sum[4] and len(sout) == 16:
            print(ol, il, sum, sout)


def _main():
    outer = [9, 8, 7, 6, 10]
    inner = [5, 4, 3, 2, 1]
    iref = [0, 1, 2, 3, 4, 0]

    for ol in itertools.permutations(outer):
        for il in itertools.permutations(inner):
            sum = [0, 0, 0, 0, 0]
            sout = ""
            for c, o in enumerate(ol):
                sum[c] = o + il[iref[c]] + il[iref[c+1]]
                sout = "{}{}{}{}".format(sout, o, il[iref[c]],il[iref[c+1]])

            if sum[0] == sum[1] == sum[2] == sum[3] == sum[4]:
                print(ol, il, sum, sout)

