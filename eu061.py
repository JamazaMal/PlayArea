nums = [set(), set(), set(), set(), set(),set()]


def buildnums():
    global nums
    i = 0
    n3 = 0
    while n3 < 10000:
        i = i + 1
        n8 = i * ((i * 3) - 2)
        if n8 > 999:
            if n8 < 10000:
                nums[5].add(int(n8))
            n7 = i * ((i * 5) - 3) / 2
            if n7 > 999:
                if n7 < 10000:
                    nums[4].add(int(n7))
                n6 = i * ((i * 2) - 1)
                if n6 > 999:
                    if n6 < 10000:
                        nums[3].add(int(n6))
                    n5 = i * ((i * 3) - 1) / 2
                    if n5 > 999:
                        if n5 < 10000:
                            nums[2].add(int(n5))
                        n4 = i * i
                        if n4 > 999:
                            if n4 < 10000:
                                nums[1].add(int(n4))
                            n3 = i * (i + 1) / 2
                            if 10000 > n3 > 999:
                                nums[0].add(int(n3))


def findsolution(_used, _sol):
    if all(_used):  # Solution probably found
        if str(_sol[0])[:2] == str(_sol[5])[2:]:
            print(_sol, _used, sum(_sol))
            return True

    for i in range(6):
        if _sol[i] == 0:
            break
    #  i = the sol we need to populate next

    if i == 0:
        for j in nums[0]:
            if findsolution([True,False,False,False,False,False], [j,0,0,0,0,0]):
                return True
    else:
        for t, b in enumerate(_used):
            if not b:
                for j in nums[t]:
                    if str(_sol[i-1])[2:] == str(j)[:2]:
                        _sol[i] = j
                        _used[t] = True
                        if findsolution(_used, _sol):
                            return True
                        _used[t] = False
                        _sol[i] = 0
    return False


def main():
    buildnums()
    findsolution([False,False,False,False,False,False], [0,0,0,0,0,0])
