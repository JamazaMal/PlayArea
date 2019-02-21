import csv

romDig = {'I': 1,
          'V': 5,
          'X': 10,
          'L': 50,
          'C': 100,
          'D': 500,
          'M': 1000}

intDig = {1000: 'M',
          900: 'CM',
          500: 'D',
          400: 'CD',
          100: 'C',
          90: 'CX',
          50: 'L',
          40: 'XL',
          10: 'X',
          9: 'IX',
          5: 'V',
          4: 'IV',
          1: 'I'}

def readfile():
    with open("089.txt", 'r') as myFile:
        for i in csv.reader(myFile, delimiter=','):
            yield i[0], int2rom(rom2int(i[0]))


def rom2int(s):
    pv = 0
    rs = 0
    for c in s:
        v = romDig[c]
        if v > pv:
            rs -= 2 * pv
        rs += v
        pv = v
    return rs


def int2rom(n):
    rs = ""
    for k in intDig:
        while n >= k:
            n -= k
            rs += intDig[k]
    return(rs)


def main():
    result = 0
    for lr, sr in readfile():
        result += len(lr) - len(sr)
    print(result)
