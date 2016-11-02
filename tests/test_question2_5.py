import pytest

from chapter2.question2_5 import sum_small_to_big, sum_big_to_small


@pytest.mark.parametrize("list_1, list_2, expected", [
    ([7, 1, 6], [5, 9, 2], 912),
    ([6, 1, 7], [2, 9, 5], 1308)
])
def test_big_to_small(list_1, list_2, expected):
    total = sum_small_to_big(list_1, list_2)
    assert (total == expected)


@pytest.mark.parametrize("list_1, list_2, expected", [
    ([7, 1, 6], [5, 9, 2], 1308),
    ([6, 1, 7], [2, 9, 5], 912)
])
def test_small_to_big(list_1, list_2, expected):
    total = sum_big_to_small(list_1, list_2)
    assert (total == expected)
