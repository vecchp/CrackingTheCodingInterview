from collections import deque


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def get_combs(pre, lst, out=None):
    if out is None:
        out = []

    if pre is None:
        pre = []

    if not lst:
        return out.append(pre)

    for i, c in enumerate(lst):
        get_combs(pre+[c], lst[:i] + lst[i + 1:], out)
    return out


def array_order(teirs):
    pre = None
    for level in teirs:

        post = get_combs(None, level)
        if pre is None:
            pre = post
        else:
            new_pre = []
            for element in pre:
                for p in post:
                    new_pre.append(element + p)
            pre = new_pre
    return pre


def get_tiers(n, cur_level=0, teirs=None):
    if not n:
        return

    if not teirs:
        teirs = []

    if len(teirs) == cur_level:
        teirs.append([n.value])
    else:
        teirs[cur_level].append(n.value)

    get_tiers(n.left, cur_level + 1, teirs)
    get_tiers(n.right, cur_level + 1, teirs)

    return teirs


def main():
    n1, n2, n3, n4, n5 = Node('1'), Node('2'), Node('3'), Node('4'), Node('5')

    n3.left = n2
    n2.left = n1
    n3.right = n5
    n5.left = n4

    teirs = get_tiers(n3)
    print(teirs)
    #print(get_combs([], ['1', '2', '3']))
    print(array_order(teirs))

    # rint(array_order(teirs))
    # results = array_order(n2)

    # for result in results:
    #    print(result)


if __name__ == '__main__':
    main()
