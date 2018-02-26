

def nodups(s):
    cc = []
    for c in str(s):
        if c in cc or c == "0":
            return False
        cc = cc + [c]
    return True


def main():
    res = set()
    for k in range(1234, 9877):
        if nodups(k):
            for i in range(1, 99):
                if k % i == 0:
                    j = k//i
                    if nodups(str(i) + str(j) + str(k)) and len(str(i) + str(j) + str(k)) == 9:
                        res.add(k)
    print(sum(res))
