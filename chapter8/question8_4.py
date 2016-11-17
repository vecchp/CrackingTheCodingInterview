def get_subsets(lst, start, end, cur, subsets):
    if start >= end:
        return subsets

    for i in range(start, end):
        tmp = cur + lst[i]
        subsets.add(tmp)
        get_subsets(lst, 1 + i, end, tmp, subsets)

    return subsets


def bin_to_set(number, lst):
    i = 0
    output = []
    while number != 0:
        if number & ~(~0 << 1):
            output.append(lst[i])
        number >>= 1
        i += 1
    return ''.join(output)


def get_subsets_2(lst):
    num_subs = 1 << len(lst)
    all_subsets = set()
    for i in range(0, num_subs):
        subset = bin_to_set(i, lst)
        all_subsets.add(subset)

    return all_subsets


def main():
    lst = ['a', 'b', 'c', 'd', 'e', 'f']
    print(sorted(get_subsets(lst, 0, len(lst), "", set())))
    print(sorted(get_subsets_2(lst)))


if __name__ == "__main__":
    main()
