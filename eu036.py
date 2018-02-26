def main():
    s = 0
    for ll in range(1, 1000000):
        ss = str(ll)
        if ss == ss[::-1]:
            bb = bin(ll)[2::]
            if bb == bb[::-1]:
                print("{}-{}".format(ll, bb))
                s = s + ll
    print(s)