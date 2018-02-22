
def prime_sieve(n):
    sieve = [True] * (n+1)
    sieve[0],sieve[1] = [False] * 2
    for i, v in enumerate(sieve):
        if v:
            sieve[i*2::i] = [False] * ((n//i)-1)
    return [i for i, v in enumerate(sieve) if v]


def f(a, b, n):
    return (n*n) + (a*n) + b


def main():
    ps = prime_sieve(100000)
    bst = 0
    for j in ps:
        if j < 1001:
            for i in range(-999, 1000, 2):
                n = 0
                while f(i, j, n) in ps:
                    n = n + 1
                if n > bst:
                    bst = n
                    print("n^2 + {}n + {} | {} primes. ({})".format(i, j, n, i*j))
