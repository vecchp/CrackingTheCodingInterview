def list_check(s):
    checker = [False] * 26
    for c in s:
        idx = ord(c) - 97
        checker[idx] ^= True

    numtrue = checker.count(True)
    if numtrue > 1:
        return False
    else:
        return True


def bits(n):
    while n:
        b = n & (~n + 1)
        yield b
        n ^= b


def bit_arithmatic(s):
    checker = 0
    for c in s:
        idx = ord(c) - 97
        checker ^= (1 << idx)

    return len(list(bits(checker))) <= 1


def bit_arithmetic(s):
    checker = 0
    num_possitive = 0
    for c in s:
        idx = ord(c) - 97
        checker ^= (1 << idx)

    return len(list(bits(checker))) <= 1


# http://stackoverflow.com/questions/3160659/innovative-way-for-checking-if-number-has-only-one-on-bit-in-signed-int
def bit_arithmetic2(s):
    checker = 0
    for c in s:
        idx = ord(c) - 97
        checker ^= (1 << idx)

    return checker == (checker & -checker)


def bit_arithmetic3(s):
    checker = 0
    for c in s:
        idx = ord(c) - 97
        checker ^= (1 << idx)

    return checker & (checker - 1) == 0


s = 't'.lower()
print(bit_arithmetic3(s))
