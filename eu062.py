
def main():
    cubes = []
    sortedcubes = []

    for i in range(10000):
        c = i**3
        cubes.append(str(c))
        sortedcubes.append("".join(sorted(list(l for l in str(c)))))

    for i in cubes:
        s = "".join(sorted(list(l for l in i)))
        c = sum(1 for l in sortedcubes if l == s)
        if c == 5:
            print(i, c)
            break

