import time
import eu043 as PB

st = time.time()
n = 1
for i in range(n):
    PB.main()
print("Duration : {} seconds.".format((time.time()-st)/n))
