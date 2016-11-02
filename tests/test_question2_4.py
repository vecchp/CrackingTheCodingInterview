import pytest

from chapter2.linked_list import generate_list
from chapter2.question2_4 import partition_1

testdata = [
    ([3, 5, 8, 5, 10, 2, 1], 5),
    ([3, 5, 8, 5, 10, 2, 1], 1)
]


@pytest.mark.parametrize("test_input, partition", testdata)
def test_partition_1(test_input, partition):
    lst = generate_list(test_input)

    partition_1(lst, partition)
    case = 0
    for node in lst:
        if node.val >= partition:
            case = 1

        if case == 0:
            assert (node.val < partition)

        if case == 1:
            assert (node.val >= partition)
