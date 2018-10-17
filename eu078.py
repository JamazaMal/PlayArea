def main():
    k = sum([[int(i * (3 * i - 1) / 2), int(i * (3 * i - 1) / 2 + i)] for i in range(1, 250)], [])

    p = [1]
    sgn = [1, 1, -1, -1]

    n = 0
    while p[n] > 0:
        n += 1
        px = 0
        i = 0
        while k[i] <= n:
            px += p[n - k[i]] * sgn[i % 4]
            i += 1
        p.append(px % 1000000)

    print(n)
