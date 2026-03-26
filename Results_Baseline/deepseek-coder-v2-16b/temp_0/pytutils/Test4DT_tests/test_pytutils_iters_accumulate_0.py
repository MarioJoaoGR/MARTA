# Module: pytutils.iters
import pytest
import operator
from pytutils.iters import accumulate

# Test cases for the accumulate function with default addition
def test_accumulate_default():
    assert list(accumulate([1, 2, 3, 4, 5])) == [1, 3, 6, 10, 15]

# Test cases for the accumulate function with multiplication
def test_accumulate_multiplication():
    assert list(accumulate([1, 2, 3, 4, 5], operator.mul)) == [1, 2, 6, 24, 120]

# Test cases for the accumulate function with an empty iterable
def test_accumulate_empty():
    assert list(accumulate([])) == []

# Additional test cases to cover different scenarios
def test_accumulate_string_concatenation():
    assert list(accumulate(['a', 'b', 'c'])) == ['a', 'ab', 'abc']

def test_accumulate_float_addition():
    assert list(accumulate([1.5, 2.5, 3.5, 4.5])) == [1.5, 4.0, 7.5, 12.0]

# Test case to ensure the function handles different types correctly
def test_accumulate_mixed_types():
    with pytest.raises(TypeError):
        list(accumulate([1, 'a', 3]))
