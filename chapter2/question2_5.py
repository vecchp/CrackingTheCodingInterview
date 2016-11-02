

# Question 2.5
# Time O(n)
# Space O(1)
def sum_small_to_big(list_1: list, list_2: list):
    order = 1
    total = 0

    for a, b in zip(list_1, list_2):
        total += (a + b) * order
        order *= 10

    return total


# Time O(n)
# Spac O(1)
def sum_big_to_small(list_1: list, list_2: list):
    total = 0
    order = 10

    for a, b in zip(list_1, list_2):
        total = total * order + a + b

    return total
