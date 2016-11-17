def find_perms(leftover, cur_perm, all_perms):
    if not leftover:
        all_perms.append(cur_perm)
        # return all_perms

    for i, c in enumerate(leftover):
        cpy = [x for j, x in enumerate(leftover) if j != i]
        find_perms(cpy, cur_perm[:] + [c], all_perms)

    return all_perms


def main():
    lst = ['a','b', 'b', 'f','w','q', 'z', 'f','c']
    perms = find_perms(lst, [], [])
    print(perms)


if __name__ == "__main__":
    main()
