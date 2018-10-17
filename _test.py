def howmanyways(distance, steps):
    if distance < 2:
        return 1
    nums = [1] + [0] * distance
    for i in range(1, distance+1):
        for j in steps:
            if i-j >= 0:
                nums[i] += nums[i-j]

    return nums[distance]


def recc(s):
    d = {}
    for c in s:
        if c in d:
            return c
        d[c] = True
    return


def main():
    print(recc('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMONPQRSTUVWXYZ1234567890ba'))
