import time


def tri(n):
    return n * (n+1) / 2


def cdiv(n):
    c = 2
    for i in range(2, (int(n**0.5))):
        if n % i == 0:
            c = c + 2
    if int(n**0.5) == (n**0.5):
        c = c + 1
    return c


def main():
    st = time.time()
    for i in range(7, 100000):
        z = tri(i)
        x = cdiv(z)
        if x > 500:
            print("{0} - {1} - {2} - {3} seconds.".format(i, int(z), x, time.time() - st))
            break

