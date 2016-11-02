import pytest

from chapter2.linked_list import generate_list
from chapter2.question2_3 import delete_in_middle

testdata = [
    ([1, 2, 3, 4], 1, [1, 3, 4]),
    ([1, 2, 3, 4], 2, [1, 2, 4]),
    ([1, 2, 3, 4], 3, [1, 2, 3, 4])
]


@pytest.mark.parametrize("test_input, distance, expected", testdata)
def test_delete_in_middle(test_input, distance, expected):
    lst = generate_list(test_input)

    node = lst.get_at_index(distance)
    delete_in_middle(node)

    for i, node in enumerate(lst):
        assert (expected[i] == node.val)
