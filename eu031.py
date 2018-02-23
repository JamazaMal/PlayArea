svl = 200                            # Value to look for
den = [ 2, 5, 10, 20, 50, 100, 200]  # Coin values
val = [-1, 0,  0,  0,  0,   0,   0]  # Number of each type of coin
cnt = 0


def nextVal(n=0): # n is the 'coins' we're currently on.
    global val
    global cnt

    if n == len(den): # We've tried all coin types
        return

    # First, go all the way up, counting each.
    val[n] = val[n] + 1
    while sum(val[i] * den[i] for i in range(0, len(den))) <= svl:
        val[n] = val[n] + 1
        cnt = cnt + 1

    # .. then go down one step at a time, calling the next 'coin', without counting.
    while val[n] > 0:
        val[n] = val[n] - 1
        nextVal(n+1)


def main():
    nextVal()
    print(cnt)
