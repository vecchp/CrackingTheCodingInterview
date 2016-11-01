import pytest

from chapter2.linked_list import Node, LinkedList
from chapter2.question2_2 import kth_away

testdata = [
    ([1, 2, 3, 4], 0, 4),
    ([1, 2, 3, 4], 1, 3),
    ([1, 2, 3, 4], 2, 2),
    ([1, 2, 3, 4], 3, 1),
    ([1, 2, 3, 4], 5, None)
]


def generate_list(input_data):
    lst = LinkedList()
    for val in input_data:
        tmp_node = Node(val)
        lst.add(tmp_node)
    return lst


@pytest.mark.parametrize("test_input, distance, expected", testdata)
def test_kth_away(test_input, distance, expected):
    lst = generate_list(test_input)

    kth = kth_away(lst, distance)

    assert(kth is expected or kth.val == expected)

