def shift_to_end(A):
    start = 0
    while A[start] is not None:
        start += 1

    for old, new in zip(range(0, start), range(start, len(A))):
        A[new] = A[old]
        A[old] = None
    return A, start


def merge(A, B):
    A, start = shift_to_end(A)

    itr, a_itr, b_itr = 0, start, 0

    a_val = A[a_itr]
    b_val = B[b_itr]
    while itr < len(A):
        if not b_val or a_val and a_val < b_val:
            A[itr] = a_val
            a_itr += 1
            a_val = A[a_itr] if a_itr < len(A) else None
        else:
            A[itr] = b_val
            b_itr += 1
            b_val = B[b_itr] if b_itr < len(B) else None
        itr += 1
    return A


def merge_2(A, B):
    a_itr = 0
    while A[a_itr] is not None:
        a_itr += 1

    a_itr -= 1
    b_itr = len(B) - 1
    a_val = A[a_itr]
    b_val = B[b_itr]

    itr = len(A) - 1
    while itr >= 0:
        if not b_val or a_val and a_val > b_val:
            A[itr] = a_val
            a_itr -= 1
            a_val = A[a_itr] if a_itr >= 0 else None
        else:
            A[itr] = b_val
            b_itr -= 1
            b_val = B[b_itr] if b_itr >= 0 else None
        itr -= 1
    return A


def main():
    A = [2, 3, 10, 50, None, None, None]
    B = [1, 6, 11]

    print(merge_2(A, B))


if __name__ == "__main__":
    main()
