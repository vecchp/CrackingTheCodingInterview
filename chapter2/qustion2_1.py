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
