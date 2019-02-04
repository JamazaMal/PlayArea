import numpy as np


def normalize(_in):
    t = sum(_in)
    _out = _in / t
    return _out


def main():
    # Solving following system of linear equation
    # 1a + 1b = 35
    # 2a + 4b = 94

    a = np.array([[1, 1], [2, 4]])
    b = np.array([35, 94])

    print(np.linalg.solve(a, b))


def _main():

    s = np.array([[0, 0, 0, 1], [.5, 0, 0, 0], [.5, 0, 0, 0], [0, 1, 1, 0]])
    d = normalize(np.array([1, 1, 1, 1]))

    for _ in range(10):
        print(d)
        d = normalize(np.dot(s, d))

    print(d)
