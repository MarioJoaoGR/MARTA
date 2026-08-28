
import pytest
from ansible.module_utils.common.collections import count

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

# Test Scenario 1: Counting elements in a list
def test_count_list():
    result = count([1, 2, 2, 3, 3, 3])
    assert result == {1: 1, 2: 2, 3: 3}

# Test Scenario 2: Counting elements in a string

# Test Scenario 3: Counting elements in a tuple
def test_count_tuple():
    result = count((1, 2, 2, 3, 3, 3))
    assert result == {1: 1, 2: 2, 3: 3}

# Test Scenario 4: Counting elements in a set

# Test Scenario 5: Raising an exception for a non-iterable argument