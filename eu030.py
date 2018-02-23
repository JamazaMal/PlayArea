dc = 6  # Max number of digits
pw = 5  # Which power to use
pows = [i**pw for i in range(0, 10)]
digits = [1] + [0] * (dc-1)


def nextDigit(n):
    global digits
    r = True
    if n == dc:
        return False
    if digits[n] == 9:
        r = nextDigit(n+1)
        if r:
            digits[n] = 0

    else:
        digits[n] = digits[n] + 1
    return r


def main():
    t = 0
    while nextDigit(0):
        p = sum(pows[i] for i in digits)
        d = sum(digits[i] * (10**i) for i in range(0, dc))
        if p == d:
            t = t + p
            print("{} - {} - {}".format(p, digits, d))
    print(t)