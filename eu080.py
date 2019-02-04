from math import log10


def srt(n, d):
    a = 5 * n
    b = 5
    while log10(b) < d+1:
        if a >= b:
            a = a - b
            b = b + 10
        else:
            a = a * 100
            b = int(str(b)[0:int(log10(b))] + "05")
    return str(b)[0:d]


def main():

    s = 0
    for i in range(1, 101):
        if (i ** 0.5) != int(i ** 0.5):
            s += sum([int(k) for k in srt(i, 100)])
    print(s)
