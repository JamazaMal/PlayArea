def main():
    best = 0
    longest = 0
    mx = 1000000
    ll = [0] * (mx+1)
    for i in range(1, mx+1):
        ll[i*2::i] = [j+i for j in ll[i*2::i]]

    for j in range(2, mx+1):
        i = ll[j]
        fnd = []
        l = 1
        while i != j and i > 0 and i <= mx and i not in fnd:
            l = l + 1
            fnd.append(i)
            i = ll[i]

        if l > longest and j == i:
            longest = l
            best = j

    print(longest, best)
