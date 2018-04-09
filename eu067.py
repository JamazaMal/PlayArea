

def main():

    tri = list()
    with open('067.txt', 'r') as f:
        for l in f:
            tri = tri + [[int(i) for i in l.split(' ')]]

    for i in range(len(tri)-2, -1, -1):
        for j in range(len(tri[i])):
            tri[i][j] = tri[i][j]  + max([tri[i+1][j], tri[i+1][j+1]])

    print(tri[0])


