"""def check_balanced(s, schema):
    opens = []
    for c in s:
        if c in schema:
            check = opens.pop() if opens else None
            if schema[c] != check:
                return False
        else:
            opens.append(c)

    return len(opens) == 0


def main():
    schema = {')': '('}
    print(check_balanced('()', schema))
    print(check_balanced('()()', schema))
    print(check_balanced(')(()', schema))

"""


def get_ways(n, num_open=0, num_close=0, cur="", ways=None):
    if ways is None:
        ways = []

    if num_open == n and num_close == n:
        ways.append(cur)
        return ways

    if num_open < n:
        get_ways(n, num_open + 1, num_close, cur + '(', ways)

    if num_open - num_close > 0:
        get_ways(n, num_open, num_close + 1, cur + ')', ways)

    return ways


if __name__ == "__main__":
    print(get_ways(10))
