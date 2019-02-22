def is_prime(n):
    return all(n % i for i in range(2, int(n**(1/2))+1))


def main():
    lst = {}
    upto = 50000000
    p2 = [i**2 for i in range(2, int(upto**(1/2)+1)) if is_prime(i)]
    p3 = [i**3 for i in range(2, int(upto**(1/3)+1)) if is_prime(i)]
    p4 = [i**4 for i in range(2, int(upto**(1/4)+1)) if is_prime(i)]

    for n4 in p4:
        i3 = 0
        while i3 < len(p3) and n4 + p3[i3] < upto:
            n3 = p3[i3]
            i2 = 0
            while i2 < len(p2) and n4 + n3 + p2[i2] < upto:
                lst[n4 + n3 + p2[i2]] = True
                i2 += 1
            i3 += 1

    print(len(lst))


if __name__ == "__main__":
    main()
