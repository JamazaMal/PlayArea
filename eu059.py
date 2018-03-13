def cntr(hnd):
    h = {}
    for i in hnd:
        h[i] = h.get(i, 0) + 1
    ret = [(h[i], i) for i in h]
    return sorted(ret, reverse=True)


def encrypt(message, key):
    ret = ""
    for i, m in enumerate(message):
        ret = ret + chr(int(m) ^ ord(key[i%len(key)]))
    return ret


def main():
    password_length = 3
    tot = 0
    password = ""
    message = list(line.split(",") for line in open('059.txt'))[0]
    print(message)
    for k in range(password_length):
        message_segment = message[k::password_length]
        z = (int(cntr(message_segment)[0][1]) ^ ord(' '))
        password = password + (chr(z))
        tot = tot + sum(int(x) ^ z for x in message_segment)

    print("Message : {}".format(encrypt(message,password)))
    print("Password : {}".format(password))
    print("Result : {}".format(tot))
