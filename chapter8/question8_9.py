
def check_balanced(s, schema):
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

if __name__ == "__main__":
    main()