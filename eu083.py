import csv

def main():
    sol = [0] * 80
    with open("083.txt", 'r') as myFile:
        data = [[int(j) for j in i] for i in csv.reader(myFile, delimiter=',')]

    for c in range(0, 79):
        print(data[0][c])
