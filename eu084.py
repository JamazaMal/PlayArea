import random
result = [0] * 40
chanceCard = 0
ccCard = 0
doubles = 0  # How many doubles rolled in a row.


def comchest(_sq):  # community chest helper
    global ccCard
    global doubles
    ccCard = (ccCard + 1) % 16
    if ccCard == 1:  # Advance to Go
        _sq = 0
    if ccCard == 2:  # Go to jail
        _sq = 10
        doubles = 0
    return _sq


def chance(_sq):  # chance helper
    global chanceCard
    global doubles
    chanceCard = (chanceCard+1) % 16
    if chanceCard == 1:  # Advance to Go
        _sq = 0
    if chanceCard == 2:  # Go to jail
        _sq = 10
        doubles = 0
    if chanceCard == 3:
        _sq = 11
    if chanceCard == 4:
        _sq = 24
    if chanceCard == 5:
        _sq = 39
    if chanceCard == 6:
        _sq = 5
    if chanceCard in [7, 8]:  # Go to NEXT railroad
        if _sq == 7:
            _sq = 15
        if _sq == 22:
            _sq = 25
        if _sq == 36:
            _sq = 5
    if chanceCard == 9:      # Go to next utility
        if _sq == [7, 36]:
            _sq = 12
        if _sq == 22:
            _sq = 28
    if chanceCard == 10:
        _sq = (_sq - 3) % 40

    return _sq


def main():
    sqr = 0                         # What square are we on now.
    global doubles
    ii = 200000
    doubles = 0
    for _ in range(ii):
        d1, d2 = random.randint(1, 4), random.randint(1, 4)
        if d1 == d2:
            doubles += 1
        else:
            doubles = 0
        if doubles == 3:
            sqr = 10
            doubles = 0
        else:
            sqr = (sqr + d1 + d2) % 40
            if sqr in [7, 22, 36]:  # Chance
                sqr = chance(sqr)
            if sqr in [2, 17, 33]:  # Community chest
                sqr = comchest(sqr)
            if sqr == 30:  # Go to jail
                doubles = 0
                sqr = 10

        result[sqr] += 1

    print(result)
    for _ in range(4):
        x = max(result)
        i = result.index(x)
        print(i, (x/ii)*100)
        result[i] = 0
