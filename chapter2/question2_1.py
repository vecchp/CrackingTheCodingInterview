from chapter2.linked_list import LinkedList


def remove_dupes_set(lst: LinkedList):
    checker = set()
    cur = lst.head
    prev = None

    while cur is not None:
        if cur.val in checker:
            prev.next = cur.next
            if cur.next is None:
                lst.tail = prev
        else:
            checker.add(cur.val)
            prev = cur
        cur = cur.next


def remove_dupes_pythonic(lst: LinkedList):
    checker = set()
    checker_add = checker.add
    return [x for x in lst if not (x.val in checker or checker_add(x.val))]


def remove_dupes_no_temp(lst: LinkedList):
    node_to_check = lst.head
    while node_to_check is not None:
        prev = node_to_check
        checker = node_to_check.next
        while checker is not None:
            if checker.val == node_to_check.val:
                prev.next = checker.next
                if checker.next is None:
                    lst.tail = prev
            else:
                prev = checker
            checker = checker.next
        node_to_check = node_to_check.next

