import pytest

from chapter2.linked_list import Node, LinkedList
from chapter2.qustion2_1 import remove_dupes_set, remove_dupes_no_temp, removed_dupes_pythonic

testdata = [
    ([1, 1], [1]),
    ([1, 1, 2], [1, 2]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 3, 4, 3, 5, 6], [1, 3, 4, 5, 6])
]


def generate_list(input_data):
    lst = LinkedList()
    for val in input_data:
        tmp_node = Node(val)
        lst.add(tmp_node)
    return lst


# Question 2.1 Using Set
# Time O(n)
# Space O(n)
@pytest.mark.parametrize("test_input,expected", testdata)
def test_remove_dupes_set(test_input, expected):
    lst = generate_list(test_input)

    remove_dupes_set(lst)

    for i, node in enumerate(lst):
        assert (expected[i] == node.val)

# Question 2.1 Pythonic
@pytest.mark.parametrize("test_input,expected", testdata)
def test_remove_dupes_pythonic(test_input, expected):
    lst = generate_list(test_input)

    lst = removed_dupes_pythonic(lst)

    for i, node in enumerate(lst):
        assert (expected[i] == node.val)


# Question 2.1 No temporary data structure
@pytest.mark.parametrize("test_input,expected", testdata)
def test_remove_dupes_set(test_input, expected):
    lst = generate_list(test_input)

    remove_dupes_no_temp(lst)

    for i, node in enumerate(lst):
        assert (expected[i] == node.val)
