def is_prime(n):
    return all(n % i for i in range(2, int(n**.5)+1))


def main():
    i = 1
    t = 0
    c = 0
    while True:
        s = i * i
        t = t + 4
        for j in range(1,4):
            if is_prime(s + ((i+1)*j)):
                c = c + 1
        if c/t < 0.1:
            print(i, t, c, c/t)
            return
        i = i + 2

