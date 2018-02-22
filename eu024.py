mx = 10
ll = list(range(0, mx))
sol = [-1] * (mx)
cnt = 0
run = True


def nextLex(d):
    global sol
    global cnt
    global run

    if not run:
        return

    if d == mx-1:  # Lex found
        cnt = cnt + 1
        if cnt == 1000000:
            print("{}-{}".format(cnt, sol))
            run = False
        return
    for i in ll:
        if i not in sol:
            sol[d+1] = i
            nextLex(d+1)
            sol[d+1] = -1


def main():
    nextLex(-1)
