def nPent(i):
    return i * (3*i - 1) / 2


def nHex(i):
    return i*((i*2) - 1)


def main():
    ih = 144
    ip = 2
    vh = nHex(ih)
    vp = nPent(ip)
    while not vh == vp:
        if vp < vh:
            ip = ip + 1
            vp = nPent(ip)
        else:
            ih = ih + 1
            vh = nHex(ih)
    print(ih, vh)
