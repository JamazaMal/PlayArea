def nx(n, d):
    return (d*2+n), (d+n)

def main():
    i = 3
    j = 2
    c = 0
    for x in range(1001):
        if len(str(i)) > len(str(j)):
            c = c + 1
        i, j = nx(i, j)

    print(c)