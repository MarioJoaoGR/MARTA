
import pytest
from string_utils.generation import random_string
import string

def test_valid_case():
    # Test with size 5
    result = random_string(5)
    assert len(result) == 5 and all(c in string.ascii_letters + string.digits for c in result)

    # Test with size 10
    result = random_string(10)
    assert len(result) == 10 and all(c in string.ascii_letters + string.digits for c in result)

    # Test with size 20
    result = random_string(20)
    assert len(result) == 20 and all(c in string.ascii_letters + string.digits for c in result)

def test_edge_cases():
    # Test with minimum size of 1
    result = random_string(1)
    assert len(result) == 1 and all(c in string.ascii_letters + string.digits for c in result)

    # Test with a large size of 100
    result = random_string(100)
    assert len(result) == 100 and all(c in string.ascii_letters + string.digits for c in result)

def test_invalid_inputs():
    # Test with None
    with pytest.raises(ValueError):
        random_string(None)

    # Test with -1
    with pytest.raises(ValueError):
        random_string(-1)

    # Test with 0
    with pytest.raises(ValueError):
        random_string(0)

    # Test with 3.5 (float)
    with pytest.raises(ValueError):
        random_string(3.5)

    # Test with 'string' (non-integer)
    with pytest.raises(ValueError):
        random_string('string')

    # Test with [1,2,3] (list)
    with pytest.raises(ValueError):
        random_string([1, 2, 3])
