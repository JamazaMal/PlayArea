def is_prime(n):
    return all(n % i for i in range(2, int(n**.5)+1))


def main():

    filset = ("AXXXB", "XAXXB", "XXAXB", "XXXAB")
    filset += ("ABXXXC", "AXBXXC", "AXXBXC", "AXXXBC")
    filset += ("XABXXC", "XAXBXC", "XAXXBC")
    filset += ("XXABXC", "XXAXBC", "XXXABC")

    for i in range(11, 1000, 2):
        for ss in filset:
            if len(ss) == 6 and i < 100:
                break

            st = ss.replace("A", str(i)[0]).replace("B", str(i)[1])
            if i > 99:
                st = st.replace("C", str(i)[2])

            if sum(is_prime(int(st.replace("X", str(k)))) for k in range(10) if k > 0 or st[0] != "X") >= 8:
                for j in range(10):
                    if is_prime(int(st.replace("X", str(j)))):
                        print(st.replace("X", str(j)))
                        return
