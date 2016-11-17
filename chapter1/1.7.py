# 90 Degree rotation
import numpy as np


def flip_ud(a):
    size = len(a)
    for i in range(size // 2):
        new_i = size - 1 - i
        for j in range(size):
            tmp = a[i][j]
            a[i][j] = a[new_i][j]
            a[new_i][j] = tmp


def swap_diag(a):
    size = len(a)
    for i in range(0, size // 2 + 1):
        for j in range(i, size):
            tmp = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = tmp


def book_answer(a):
    size = a.shape
    if a.shape[0] == 0 or a.shape[0] != a.shape[1]:
        return False

    n = a.shape[0]

    for layer in range(0, n // 2):
        last = n - 1 - layer
        for i in range(layer, last):
            offset = i - layer
            top = a[layer][i]

            # left -> top
            a[layer][i] = a[last - offset][layer]

            # bottom -> left
            a[last - offset][layer] = a[last][last - offset]

            # right -> bottom
            a[last][last - offset] = a[i][last]

            # top -> right
            a[i][last] = top


def test_fun(a):
    print(a)
    flip_ud(a)
    swap_diag(a)
    print(a)


test1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# test_fun(test1)
print(test1)
book_answer(test1)
print(test1)
test2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
# test_fun(test2)
