import time
st = time.time()

import eu078 as PB

n = 1  #  Make this number bigger more for a more accurate execution time
for _ in range(n):
    PB.main()

print("Duration : {} seconds.".format((time.time()-st)/n))
