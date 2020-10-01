from random import randint

n = 30
t = 0

for _ in range(n):
    n1 = randint(1, 12)
    n2 = randint(1, 12)
    x = n1 * n2

    r = input("{} / {} = ".format(x, n1))
    if n2 == int(r):
        print("Correct")
        t = t + 1
    else:
        print("Wrong. It's {}.".format(n2))

print("You got {} right out of {}. {}%".format(t, n, (t/n)*100))
