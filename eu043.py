import itertools


def f(n, d):
    return n[d]*100 + n[d+1]*10 + n[d+2]


def main():
    t = 0
    for nums in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        if nums[5] == 5:
            if nums[3] % 2 == 0:
                if f(nums, 7) % 17 == 0:
                    if f(nums, 6) % 13 == 0:
                        if f(nums, 5) % 11 == 0:
                            if f(nums, 4) % 7 == 0:
                                if f(nums, 2) % 3 == 0:
                                    t = t + int("".join([str(i) for i in nums]))
    print(t)