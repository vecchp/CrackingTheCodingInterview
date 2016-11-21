"""
This is wrong

def countways(n, end):
    if n > end:
        return 0

    if n == end:
        return 1

    return countways(n + 25, end) + countways(n + 10, end) + countways(n + 5, end) + countways(n + 1, end)
"""

# We can also cache this.
def countways_2(amount, index=0, denoms=[25, 10, 5, 1]):
    if index >= len(denoms) - 1:
        return 1

    denomAmount = denoms[index]
    ways = 0
    for i in range(0, amount + denomAmount, denomAmount):
        amount_remaining = amount - i * denomAmount
        ways += countways_2(amount_remaining, index + 1, denoms)

    return ways


def main():
    #print(countways(0, 10))
    print(countways_2(10))


if __name__ == '__main__':
    main()
