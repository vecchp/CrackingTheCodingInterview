import pytest

from chapter2.linked_list import generate_list
from chapter2.question2_1 import remove_dupes_set, remove_dupes_no_temp, remove_dupes_pythonic

testdata = [
    ([1, 1], [1]),
    ([1, 1, 2], [1, 2]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 3, 4, 3, 5, 6], [1, 3, 4, 5, 6])
]


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

    lst = remove_dupes_pythonic(lst)

    for i, node in enumerate(lst):
        assert (expected[i] == node.val)


# Question 2.1 No temporary data structure
# O(n^2) time
# O(1) space
@pytest.mark.parametrize("test_input,expected", testdata)
def test_remove_dupes_set(test_input, expected):
    lst = generate_list(test_input)

    remove_dupes_no_temp(lst)

    for i, node in enumerate(lst):
        assert (expected[i] == node.val)
