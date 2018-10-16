
def getPrimes(n):
    prm = [False] * (n+1)
    ret = [2]
    for i in range(3, n + 1, 2):
        if not prm[i]:
            prm[i:n+1:i] = [True] * (int(n / i))
            ret.append(i)
    return ret


def sumWays(mx):
    res = [0] * (mx+1)
    res[0] = 1
    for i in range(len(primes)):
        for j in range(primes[i], mx+1):
            res[j] = res[j] + res[j-primes[i]]
    return res[mx]

max = 100
primes = getPrimes(max)


def main():
    for i in range(max):
        if sumWays(i) > 5000:
            print(i)
            break
