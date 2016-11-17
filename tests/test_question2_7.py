import pytest

from chapter2.linked_list import generate_list
#from chapter2.question2_7 import is_palindrome

def create_intersection(list_1, list_2, from_index, to_index):
    if index < len(list_1):



@pytest.mark.parametrize("list_1, list_2, from_index, to_index, expected", [
    (['m', 'f'], ['p','q','r'], 1, True),
    (['m', 'e', 'b'], ['a','h', 'q'], -1, False),
    (['c', 'l', 'g'], ['s', 'k', 't'], 2, True),
])
def test_intersection(list_1, list_2, from_index, to_index, expected):
    list_1 = generate_list(list_1)
    list_2 = generate_list(list_2)

    ret = is_palindrome(list_1)
    assert (ret == expected)
