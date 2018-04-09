def main():
    m = 101
    for D in range(2,m):
        if (D**0.5) % 1 != 0:
            x = 1
            while True:
                x = x + 1
                y = ((x**2)/D) - (1/D)
                if (y**0.5)%1 == 0:
                    print("{}^2 - ({} * {}^2) = 1".format(x, D, int(y**0.5)))
                    break



def _main():
    m = 11
    r1 = [[[D, (D * (i**2)) + 1] for i in range(1, m)] for D in range(2, m) if (D**0.5) % 1 != 0]

    print(r1)

