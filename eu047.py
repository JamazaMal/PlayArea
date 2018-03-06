
def fct(n):
    i = n
    x = 2
    ret = set()
    while i > 1 and x <= (n**.5)+1:
        while not(i % x):
            i = i // x
            ret.add(x)
        x = x + 1
    return ret

def main():
    print(fct(4722031*170000000000))
