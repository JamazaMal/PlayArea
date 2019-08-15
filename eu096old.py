import csv


def readboard():
    c = 0
    res = []
    with open("096.txt", 'r') as myFile:
        for i in csv.reader(myFile, delimiter=','):
            if c > 0:
                res.append([int(j) for j in i[0]])
            c += 1
            if c > 9:
                c = 0
                yield res
                res = []


def isValid(brd, x, y, v):
    if v in [brd[i][x] for i in range(9)]:
        return False
    if v in [brd[y][i] for i in range(9)]:
        return False

    i = x//3
    j = y//3
    for k in range(i, i+3):
        for l in range(j, j+3):
            if brd[l][k] == v:
                return False
    return True


def solve(b):
    print(b)
    if all(0 not in p for p in b):
        print("boogie")
        return b
    for x in range(9):
        for y in range(9):
            if b[y][x] == 0:
                for v in range(1, 9):
                    if isValid(b, x, y, v):
                        b[y][x] = v
                        ret = solve(b)
                        if ret != 0:
                            return ret
                b[y][x] = 0
    return 0


def main():
    for i, b in enumerate(readboard()):
        print(i, solve(b))
        break
