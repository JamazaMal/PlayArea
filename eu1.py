import time


def prime_sum(n):
    pr = [True] * (n+1)
    pr[0], pr[1] = [False] * 2
    s = 0
    for num, ip in enumerate(pr):
        if ip:
            s = s + num
            #Silly test
            pr[num*2::num] = [False] * (n//num-1)
    return s


st = time.time()
print("{0} in {1} seconds".format(prime_sum(2000000), time.time()-st))