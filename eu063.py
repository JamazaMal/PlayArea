def _main():
    cnt = 0
    ocnt = -1
    n = 0
    while not cnt == ocnt:
        ocnt = cnt
        n = n + 1
        cnt = cnt + sum([n == len(str(b ** n)) for b in range(1, 10)])

    print(cnt)

def main():
    i = 0
    cnt = 0
    fnd = True
    while fnd:
        fnd = False
        i = i + 1
        for n in range(1, 10):
            if len(str(n ** i)) == i:
                cnt = cnt + 1
                fnd = True

    print(cnt)