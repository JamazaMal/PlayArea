
def isBad(p1, p2, p3, p4):
    return not((p2 < p3) or (p4 < p1))


def main():
    print("1 - {0}".format(isBad(1, 2, 3, 4)))
    print("2 - {0}".format(isBad(1, 3, 2, 4)))
    print("3 - {0}".format(isBad(1, 4, 2, 3)))
    print("4 - {0}".format(isBad(2, 3, 1, 4)))
    print("5 - {0}".format(isBad(2, 4, 1, 3)))
    print("6 - {0}".format(isBad(3, 4, 1, 2)))
