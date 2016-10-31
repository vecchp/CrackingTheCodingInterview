import pytest

from chapter2.linked_list import Node, LinkedList, remove_dupes_set


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


@pytest.mark.parametrize("test_input,expected", [
    ([1, 1], [1]),
    ([1, 1, 2], [1, 2]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 3, 4, 3, 5, 6], [1, 3, 4, 5, 6])
])
def test_remove_dupes(test_input, expected):
    lst = LinkedList()
    for val in test_input:
        tmp_node = Node(val)
        lst.add(tmp_node)

    remove_dupes_set(lst)
    for i, node in enumerate(lst):
        print(i, node.val)
        assert (expected[i] == node.val)
