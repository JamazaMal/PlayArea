def rev(n):
    return int(str(n)[::-1])


def lyc(n):
    i = n + rev(n)
    c = 0
    while i != rev(i) and c < 51:
        i = i + rev(i)
        c = c + 1

    if c == 51:
        return True

    return False


def main():
    c = 0
    for i in range(10000):
        if (lyc(i)):
            c = c + 1
    print(c)