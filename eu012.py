import time
mx = 15000  # Random Search depth limit
divs = [0] * (mx)


def cdiv(n):
    global divs
    if divs[n] != 0:
        return divs[n]

    c = 2
    for i in range(2, int((n-1)**0.5)):
        if n % i == 0:
            c = c + 2
    if (n**0.5).is_integer():
        c = c + 1
    divs[n] = c
    return c


def main():
    st = time.time()
    for n in range(3, mx):
        if n % 2 == 0:
            x = cdiv(n//2) * cdiv(n+1)
            if x > 500:
                break
        else:
            x = cdiv(n) * cdiv((n+1)//2)
            if x > 500:
                break

    print("Found {0} in {1} seconds.".format(n * (n+1) / 2, time.time() - st))


main()

