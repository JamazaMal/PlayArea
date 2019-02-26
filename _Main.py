import time
st = time.time()

import eu092 as PB  # Placed here to include the time

n = 1  # Make this number bigger more for a more accurate execution time
for _ in range(n):
    PB.main()

print("Duration : {} seconds.".format((time.time()-st)/n))
