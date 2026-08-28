
import pytest
from flutes.iterator import MapList


def test_len_method():
    original_list = [1, 2, 3]
    mapped_list = MapList(lambda x: x * x, original_list)
    assert len(mapped_list) == len(original_list)

def test_element_access():
    original_list = [1, 2, 3]
    mapped_list = MapList(lambda x: x * x, original_list)
    for i in range(len(original_list)):
        assert mapped_list[i] == (original_list[i] ** 2)