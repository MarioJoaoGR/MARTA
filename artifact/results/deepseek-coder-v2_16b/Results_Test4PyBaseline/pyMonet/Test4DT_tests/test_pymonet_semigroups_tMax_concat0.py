# Module: pymonet.semigroups
import pytest
from pymonet.semigroups import Max

# Test cases for the Max class
def test_max_initialization():
    max_instance = Max(-float('inf'))
    assert max_instance.value == -float('inf')

def test_max_concat_first_larger():
    max1 = Max(5)
    max2 = Max(3)
    result = max1.concat(max2)
    assert result.value == 5

def test_max_concat_second_larger():
    max1 = Max(2)
    max2 = Max(4)
    result = max1.concat(max2)
    assert result.value == 4

def test_max_concat_equal_values():
    max1 = Max(6)
    max2 = Max(6)
    result = max1.concat(max2)
    assert result.value == 6

def test_max_concat_neutral_element():
    neutral_max = Max(-float('inf'))
    other_max = Max(5)
    result = neutral_max.concat(other_max)
    assert result.value == 5

if __name__ == "__main__":
    pytest.main()
