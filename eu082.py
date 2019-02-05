import csv

def main():
    with open("082.txt", 'r') as myFile:
        data = [[int(j) for j in i] for i in csv.reader(myFile, delimiter=',')]

    sol = [0] * len(data)

    # Initiate sol to first column
    for r in range(0, len(data)):
        sol[r] = data[r][0]

    # Manage rest of the columns
    for c in range(1, len(data[0])):
        # Check Left and up
        sol[0] = data[0][c] + sol[0]
        for r in range(1, len(data)):
            sol[r] = data[r][c] + min(sol[r], sol[r-1])

        # Check down
        for r in range(len(data)-2, -1, -1):
            sol[r] = min(sol[r], (sol[r+1] + data[r][c]))

    print(min(sol))
