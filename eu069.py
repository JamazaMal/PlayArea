def prime_sieve(n):
    sieve = [True] * (n // 2)
    for i in range(3,int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)

    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]


def phi(_i):
    z = _i
    for x in primes:
        if x > _i:
            break
        if _i % x == 0:
            z = z * (1-(1/x))

    return z


primes = prime_sieve(1000)


def main():
    best = 0
    for i in range(2, 1000000):
        j = i/phi(i)
        if j > best:
            best = j
            print("{} -- {}".format(i, j))
