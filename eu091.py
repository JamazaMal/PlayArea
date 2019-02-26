from math import gcd


def main():
    mx = 50
    res = mx * mx * 3  # Count of simple triangles
    for x in range(1, mx+1):
        for y in range(1, mx+1):
            f = gcd(x, y)
            res += min(y*f//x, (mx-x)*f//y) * 2

    print(res)
