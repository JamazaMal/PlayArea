import time
st = time.time()

import eu046 as PB

n = 1
for i in range(n):
    PB.main()
print("Duration : {} seconds.".format((time.time()-st)/n))
