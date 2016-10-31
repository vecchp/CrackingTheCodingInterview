from chapter2.linked_list import Node, LinkedList


def test_node():
    node_one = Node(1)
    assert (node_one.val == 1)
    assert (node_one.next is None)


def test_iterate():
    node_one = Node(0)
    node_two = Node(1)

    lst = LinkedList()
    lst.add(node_one)
    lst.add(node_two)

    for i, node in enumerate(lst):
        assert (i == node.val)
