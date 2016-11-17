import random


def fisher_yates(array, start=0):
    if not array or start >= len(array):
        return

    firstElementIndex = random.randrange(start, len(array))

    array[start], array[firstElementIndex] = array[firstElementIndex], array[start]
    fisher_yates(array, start + 1)


deck = [x for x in range(0, 52)]

print(deck)
fisher_yates(deck)
print(deck)
