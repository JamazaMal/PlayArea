import time
import eu031 as PB

st = time.time()
PB.main()
print("Duration : {} seconds.".format(time.time()-st))
