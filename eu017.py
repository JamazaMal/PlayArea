ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
tens = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
hundreds = [i + 7 for i in ones]
hundreds[0] = 0


def cnt(i):
    c = hundreds[i//100]
    if c > 0:
        i = i - ((i//100)*100)
        if i > 0:
            c = c + 3

    if i in range(10, 20):
        c = c + teens[i-10]
    else:
        c = c + tens[i//10]
        i = i - ((i//10)*10)
        c = c + ones[i]
    return c


def main():
    c = 0
    for i in range(1, 1000):
        c = c + cnt(i)
    c = c + 11  # Add 'ONE THOUSAND'
    print(c)

