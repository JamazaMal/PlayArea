mx = 1000
ps = [True] * (mx // 2)


def prime_sieve(n):
    sieve = [True] * (n // 2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)

    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]


def f(N):
    if N < 8:
        return 3
    for d in ps[::-1]:
        period = 1
        while pow(10, period) % d != 1: period += 1
        if d-1 == period:
            return d


def main():
    global ps
    ps = prime_sieve(mx)
    print(f(mx))
