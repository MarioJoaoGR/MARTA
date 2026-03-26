# Module: pymonet.utils
import pytest
from pymonet.utils import identity

# Test cases for the identity function
def test_identity_integer():
    result = identity(5)
    assert result == 5, f"Expected 5 but got {result}"

def test_identity_string():
    result = identity("hello")
    assert result == "hello", f"Expected 'hello' but got {result}"

def test_identity_list():
    result = identity([1, 2, 3])
    assert result == [1, 2, 3], f"Expected [1, 2, 3] but got {result}"

# Additional test case to ensure the function works with any other type
def test_identity_other_types():
    result_int = identity(123)
    assert result_int == 123, f"Expected 123 but got {result_int}"
    
    result_str = identity("example")
    assert result_str == "example", f"Expected 'example' but got {result_str}"
    
    result_list = identity([4, 5, 6])
    assert result_list == [4, 5, 6], f"Expected [4, 5, 6] but got {result_list}"
