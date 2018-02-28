import itertools


def isPrime(n):
    for i in range(2, int(n**0.5)):
        if n%i == 0 :
            return False
    return True


def main():
    for ll in itertools.permutations(["7", "6", "5", "4", "3", "2", "1"]):
        i = int("".join(ll))
        if isPrime(i):
            print(i)
            break

