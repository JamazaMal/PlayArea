
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n/i == n//i:
            return False
    return True


def isCPrime(n): # Also sum
    z = list(c for c in str(n))
    for i in range(len(z)):
        t = z[0]
        for j in range(len(z)-1):
            z[j] = z[j+1]
        z[len(z)-1] = t
        if not isPrime(int("".join(z))):
            return False
    return True


def main():
    # limited list of possibly circular primes.
    l = [1, 3, 7, 9]
    i = 0
    cnt = 4
    while i < len(l):
        if l[i] > 10:   # Check circular primeness
            if isCPrime(l[i]):
                print("{} is circ-prime {} {}".format(l[i],l[i],len(str(l[i]))))
                cnt = cnt + 1
        if l[i]*10 < 1000000:
            l = l + [l[i] * 10 + 1]
            l = l + [l[i] * 10 + 3]
            l = l + [l[i] * 10 + 7]
            l = l + [l[i] * 10 + 9]
        i = i + 1
    print(cnt)

