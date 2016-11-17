def prod(a, b):
    product = 0
    while b != 0:
        case = b & 1
        if case:
            product += a
        b >>= 1
        a <<= 1

    return product


def prod_2(a, b):
    if b == 0:
        return 0

    tmp = a if b & 1 else 0
    return tmp + prod_2(a << 1, b >> 1)


# This is pretty cool since you break it into base cases of 1 * x or 0
# Since you are dividing by 2 each time you can compute in log(smaller) time
def prod_3(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    s = smaller >> 1
    half_prod = prod_3(s, bigger)

    if smaller % 2 == 0:
        return half_prod + half_prod

    return half_prod + half_prod + bigger


def main():
    A = 50
    B = 5
    print(prod(A, B))
    print(prod_2(A, B))
    print(prod_3(A, B))


if __name__ == "__main__":
    main()
