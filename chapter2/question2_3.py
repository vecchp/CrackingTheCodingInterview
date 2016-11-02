from chapter2.linked_list import Node


# Question 2.3
# Time O(n)
# Space O(1)
def delete_in_middle(node: Node) -> bool:
    if node is None or node.next is None:
        return False

    tmp = node.next
    node.val = tmp.val
    node.next = tmp.next

    # Of course here since we are modifying the next elemetn we would have to update the tail of lst
