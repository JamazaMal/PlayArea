import csv

with open("083.txt", 'r') as myFile:
    data = [[int(j) for j in i] for i in csv.reader(myFile, delimiter=',')]

tmpData = [[1000000 for _ in range(len(data[0]))] for _ in range(len(data))]

path = {}


def stepTo(r, c, dr, dc):
    global tmpData
    global path

    if tmpData[r][c] + data[dr][dc] < tmpData[dr][dc]:
        tmpData[dr][dc] = tmpData[r][c] + data[dr][dc]
        path[(dr, dc)] = 1


def main():
    path[(0, 0)] = 1
    tmpData[0][0] = data[0][0]

    while len(path) > 0:
        r, c = next(iter(path.keys()))

        if r < len(data)-1:
            stepTo(r, c, r+1, c)
        if c < len(data[0])-1:
            stepTo(r, c, r, c+1)
        if r > 0:
            stepTo(r, c, r-1, c)
        if c > 0:
            stepTo(r, c, r, c-1)
        del(path[r, c])

    print(tmpData[len(data)-1][len(data[0])-1])