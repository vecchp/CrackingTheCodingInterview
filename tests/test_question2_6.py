import pytest

from chapter2.question2_6 import is_palindrome


@pytest.mark.parametrize("list_1, expected", [
    (['m', 'm'], True),
    (['m', 'e', 'b'], False),
    (['m', 'o', 'm'], True),
])
def test_is_palindrome(list_1, expected):
    ret = is_palindrome(list_1)
    assert (ret == expected)
