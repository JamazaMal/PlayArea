import itertools

def prime_sieve(n):
    sieve = [True] * (n // 2)
    for i in range(3,int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)

    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]


primes = prime_sieve(10**7)


def main():
    best = 1000
    for p1 in primes[445:0:-1]:
        for p2 in primes[446::]:
            if p1*p2 > 10**7:
                break
            if sorted(str(p1*p2)) == sorted(str((p1-1)*(p2-1))):
                print(p1, p2, p1 * p2)
                return

