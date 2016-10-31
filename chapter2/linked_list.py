class Node:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, n):
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def __iter__(self):
        cur_node = self.head
        while cur_node is not None:
            yield cur_node
            cur_node = cur_node.next


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

