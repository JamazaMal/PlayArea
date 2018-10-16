def main():
    mx = 100
    res = [0] * (mx+1)
    res[0] = 1
    for i in range(1, mx+1):
        for j in range(i, mx+1):
            res[j] = res[j] + res[j-i]
        print(res)

    print(res[mx])
