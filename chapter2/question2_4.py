from chapter2.linked_list import LinkedList


# Question 2.4
# Time O(n)
# Space O(1)
def partition_1(lst: LinkedList, partition: int):
    head = lst.head
    tail = lst.head

    cur_node = lst.head

    while cur_node is not None:
        _next = cur_node.next

        if cur_node.val < partition:
            cur_node.next = head
            head = cur_node
        else:
            tail.next = cur_node
            tail = cur_node

        cur_node = _next

    # Make sure you update the tails next pointer to None
    # otherwise we can have an infinite loop x.x
    tail.next = None
    lst.head = head
    lst.tail = tail
