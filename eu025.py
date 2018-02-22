import math

def main():
    i = 1
    j = 1
    t = i + j
    c = 3

    while int(math.log10(t)) < 999:
        i = j
        j = t
        c = c + 1
        t = i + j

    print("{}-{}".format(c, t))
