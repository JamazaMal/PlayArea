import csv


def main():
    with open("081.txt", 'r') as myFile:
        data = [[int(j) for j in i] for i in csv.reader(myFile, delimiter=',')]

    # Do the first line differently (Only one path)
    for c in range(1, 80):
        data[0][c] += data[0][c-1]

    # Now do the rest of the grid
    for r in range(1, 80):
        # First column in each row, can only come from one place
        data[r][0] += data[r-1][0]
        # Rest of the columns, have a choice
        for c in range(1,80):
            if data[r-1][c] < data[r][c-1]:
                data[r][c] += data[r-1][c]
            else:
                data[r][c] += data[r][c-1]

    print(data[79][79])