from functools import lru_cache

@lru_cache(maxsize=None)
def countEval(s, desired):
    """

    :param s:
    :param desired:
    :return:
    """
    if not s:
        return 0

    if len(s) == 1:
        return 1 if bool(s[0]) == desired else 0

    ways = 0

    # now we want to loop through every character in s
    for i in range(1, len(s), 2):

        c = s[i]
        left, right = s[0:i], s[i + 1:]
        left_true, left_false = countEval(left, True), countEval(left, False)
        right_true, right_false = countEval(right, True), countEval(right, False)
        """
        if c == '^':
            if desired:
                sub_ways = left_true * right_false + left_false * right_true
            else:
                sub_ways = left_true * right_true + left_false * right_false
        elif c == '&':
            if desired:
                sub_ways = left_true * right_true
            else:
                sub_ways = left_false * right_true + left_true*right_false + left_false*right_false

        elif c == '|':
            if desired:
                sub_ways = left_true * right_true + left_false * right_true + left_true * right_false
            else:
                sub_ways = left_false * right_false
        """
        # now we want to check if we are at an operator
        total = (left_true + left_false) * (right_true + right_false)
        total_true = 0
        if c == '^':
            total_true = left_true * right_false + left_false * right_true
        elif c == '&':
            total_true = left_true * right_true
        elif c == '|':
            total_true = left_true * right_true + left_false * right_true + left_true * right_false
        sub_ways = total_true if desired else total - total_true
        ways += sub_ways
    return ways


if __name__ == '__main__':
    """
    1^0|0|1 0
    1^0|0|1 1
    1&0|1^0|0|1&1&0 0
    1&0|1^0|0|1&1&0 1
    0^0|1&1^1|0|1 1
    0^0|1&1^1|0|1 0
    """

    #print(countEval('1^0|0|1', False))

    #print(countEval('1^0|0|1', False))
    #print(countEval('1^0|0|1', True))
    print(countEval('1&0|1^0|0|1&1&0', False))
    #print(countEval('1&0|1^0|0|1&1&0', True))
    #print(countEval('0^0|1&1^1|0|1', False))
    #print(countEval('0^0|1&1^1|0|1', True))

    #test = '0&0&0&1^1|0'
    #i = 9

    #print(test[:i], test[i + 1:])
