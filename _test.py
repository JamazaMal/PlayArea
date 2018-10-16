from random import seed
from random import random
import numpy as np


def half(_i):
    return _i / 2


def main():
    ins = np.array([100, 200, 300])
    print(ins)

    wts = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12]])
    print(wts)

    wts = np.random.rand(4, 3)
    print(wts)

    ots1 = (ins * wts)
    ots2 = np.sum((ins * wts), axis=1)
    ots3 = half(np.sum((ins * wts), axis=1))

    print(ots1)
    print(ots2)
    print(ots3)
