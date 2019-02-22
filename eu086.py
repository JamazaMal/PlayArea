
def main():
    target = 1000000
    cnt = 0
    x = 0
    while cnt < target:
        x += 1
        for yz in range(1, x+1):
            if (((x*x) + yz*yz)**0.5) % 1 == 0:
                cnt += yz / 2
        for yz in range(x+1, (x*2)+1):
            if (((x*x) + yz*yz)**0.5) % 1 == 0:
                cnt += 1+(x-(yz+1)/2)

    print(x)


if __name__ == "__main__":
    main()
