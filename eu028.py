def main():
    mx = 1001   # Side length of square
    c = 1
    for i in range(3, mx + 1, 2):
        c = c + (4*(i**2)) - (6*(i-1))
    print(c)
