

# Question 2.6
# Time O(n)
# Space O(1)
def is_palindrome(lst: list):

    checker = 0
    base = ord('a')

    for letter in lst:
        i = ord(letter.lower()) - base
        checker ^= (1 << i)

    #bitcheck = checker == checker & (-checker) or checker == 0
    #return bitcheck
    return checker & (checker - 1) == 0

