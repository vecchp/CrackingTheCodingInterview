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

    """
    def __iter__(self):
        self.state = self.head
        return self

    def __next__(self):
        if self.state is not None:
            ret = self.state
            self.state = self.state.next
            return ret
        else:
            raise StopIteration
    """
