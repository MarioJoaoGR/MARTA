
import pytest
from flutils.objutils import is_list_like

class CustomListLike:
    def __init__(self, items):
        self.items = items
    
    def __iter__(self):
        return iter(self.items)


def test_is_list_like_with_standard_list():
    standard_list = [1, 2, 3]
    assert is_list_like(standard_list) == True

def test_is_list_like_with_reversed_iterator():
    reversed_iter = reversed([1, 2, 3])
    assert is_list_like(reversed_iter) == True

def test_is_list_like_with_string():
    string_obj = 'hello'
    assert is_list_like(string_obj) == False

def test_is_list_like_with_sorted_sequence():
    sorted_seq = sorted('hello')
    assert is_list_like(sorted_seq) == True

def test_is_list_like_with_integer():
    integer_obj = 123
    assert is_list_like(integer_obj) == False