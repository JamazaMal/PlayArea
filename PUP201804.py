def main():
    x = 1
    tot = 1
    while tot < x*10:
        x = x + 1
        tot = tot + sum(int(i) for i in str(x))
    print(x, tot)
