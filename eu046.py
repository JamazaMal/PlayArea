def main():
    n = 3
    prm = set()
    prm.add(2)

    while True:
        if all(n % p for p in prm):
            prm.add(n)
        else:
            if not any((n - 2 * i * i) in prm for i in range(1, n)):
                break
        n = n + 2

    print(n)





