from collections import defaultdict


def num_ways(n, count):
    if count == n:
        return 1

    elif count > n:
        return 0

    return num_ways(n, count + 1) + \
           num_ways(n, count + 2) + \
           num_ways(n, count + 3)


def num_ways_dp(n, ways):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in ways:
        return ways[n]
    else:
        ways[n] = num_ways_dp(n - 1, ways) + num_ways_dp(n - 2, ways) + num_ways_dp(n - 3, ways)
        return ways[n]


def kicker_dp(n):
    ways = defaultdict(int)
    num = num_ways_dp(n, ways)
    return num


# print(num_ways(20, 0))
print(kicker_dp(6))
