from chapter2.linked_list import LinkedList, Node


# Question 2.2
# Time O(n)
# Space O(1)
def kth_away(lst: LinkedList, distance: int) -> Node:

    kth, end_check = lst.head, lst.head
    for i in range(0, distance):
        end_check = end_check.next
        if end_check is None:
            return None

    while end_check.next is not None:
        end_check = end_check.next
        kth = kth.next

    return kth
