
import pytest
from ansible.module_utils.common.collections import count

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


def test_count_list():
    assert count([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}

def test_count_tuple():
    assert count((1, 2, 2, 3, 3, 3)) == {1: 1, 2: 2, 3: 3}


def test_invalid_argument():
    with pytest.raises(Exception):
        count(12345)