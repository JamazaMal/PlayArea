def isPent(i):
    if ((((((24*i)+1)**0.5)+1)/6) + 1) % 1 == 0:
        return True
    return False


def pent(i):
    return (i*((3*i) - 1))/2


def main():
    i = 0
    found = False
    while not found:
        i = i + 1
        pi = pent(i)
        for j in range(i, 0, -1):
            pj = pent(j)
            if isPent(pi + pj):
                if isPent(pi - pj):
                    print(i, j, pi-pj)
                    found = True
                    break
