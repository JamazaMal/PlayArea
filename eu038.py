# 38 - n will be in range 9876 - 9123

def isPan(n):
    if "0" in str(n):
        return False
    for i, v in enumerate(str(n)):
        if v in (str(n)+"x")[i+1::]:
            return False
    return True

def main():
    for n in range(9876, 9122, -1):
        if isPan(int(str(n) + str((n*2)))):
            break
    print(int(str(n) + str((n*2))))
