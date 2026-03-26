# Module: pymonet.semigroups
import pytest
from pymonet.semigroups import Max  # Assuming the module is correctly imported as such

# Test initialization with neutral element and a normal value
def test_init_neutral():
    max_instance = Max(-float('inf'))
    assert max_instance.value == -float('inf')

def test_init_normal_value():
    max_instance = Max(5)
    assert max_instance.value == 5

# Test concatenation with values where self is larger
def test_concat_self_larger():
    max1 = Max(-float('inf'))
    max2 = Max(3)
    combined_max = max1.concat(max2)
    assert combined_max.value == 3

# Test concatenation with values where semigroup is larger
def test_concat_semigroup_larger():
    max1 = Max(-float('inf'))
    max2 = Max(10)
    combined_max = max1.concat(max2)
    assert combined_max.value == 10

# Test concatenation with floating-point numbers
def test_concat_with_floats():
    max1 = Max(-float('inf'))
    max2 = Max(3.14)
    combined_max = max1.concat(max2)
    assert combined_max.value == 3.14

# Test concatenation with the same value, should return either value as it is a neutral element test
def test_concat_same_values():
    max1 = Max(-float('inf'))
    max2 = Max(-float('inf'))
    combined_max = max1.concat(max2)
    assert combined_max.value == -float('inf')

# Edge case: Test concatenation with the neutral element and a normal value
def test_concat_with_neutral():
    max_instance = Max(-float('inf'))
    combined_max = max_instance.concat(Max(-float('inf')))
    assert combined_max.value == -float('inf')

# Edge case: Test concatenation with a very large value to ensure it doesn't break the concat method
def test_concat_with_large_value():
    max1 = Max(-float('inf'))
    max2 = Max(float('inf'))  # A very large value
    combined_max = max1.concat(max2)
    assert combined_max.value == float('inf')
