import pytest

from chapter2.linked_list import Node, LinkedList
from chapter2.qustion2_1 import remove_dupes_set

testdata = [
    ([1, 1], [1]),
    ([1, 1, 2], [1, 2]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 3, 4, 3, 5, 6], [1, 3, 4, 5, 6])
]


## Question 2.1
@pytest.mark.parametrize("test_input,expected", testdata)
def test_remove_dupes_set(test_input, expected):
    lst = LinkedList()
    for val in test_input:
        tmp_node = Node(val)
        lst.add(tmp_node)

    remove_dupes_set(lst)
    for i, node in enumerate(lst):
        print(i, node.val)
        assert (expected[i] == node.val)
