import numpy as np


def find_zeros(a):
    rows, cols = 0, 0
    for i in range(0, a.shape[0]):
        for j in range(0, a.shape[1]):
            is_zero = a[i][j] == 0
            rows |= is_zero << i
            cols |= is_zero << j

    return rows, cols


def zero_out(a):
    rows, cols = find_zeros(a)

    for i in range(0, a.shape[0]):
        i_bitmask = 1 << i
        for j in range(0, a.shape[1]):
            j_bitmask = 1 << j
            is_zero = (rows & i_bitmask or cols & j_bitmask) > 0
            a[i][j] *= ~is_zero

"""
We could also use the first row and column of the array as storage instead of bitvectors.
    1) Check if the first row and column have any zeros, and set the variables rowHasZero
"""


if __name__ == "__main__":
    test1 = np.array([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    # test_fun(test1)
    print(test1)
    zero_out(test1)
    print(test1)
