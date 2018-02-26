

def main():
    p = 1
    for tu in range(1, 10):
        for ou in range(1, 10):
            for td in range(tu, 10):
                for od in range(1, 10):
                    if (td*10+od)>0:
                        r = (tu*10+ou)/(td*10+od)
                        if r < 1 and r > 0:
                            if ((ou == od and td > 0 and r == (tu / td)) or
                                (tu == td and od > 0 and r == (ou / od)) or
                                (ou == td and od > 0 and r == (tu / od)) or
                                (tu == od and td > 0 and r == (ou / td))):
                                    p = p * r
                                    print("{}{} / {}{} = {}".format(tu, ou, td, od, r))
    print(p)

