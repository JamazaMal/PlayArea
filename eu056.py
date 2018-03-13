def dsum(n):
    return sum(int(i) for i in str(n))


def main():
    ms = 0
    for i in range(1, 100):
        for j in range(1, 100):
            mx = dsum(i**j)
            if mx > ms:
                ms = mx
    print(ms)