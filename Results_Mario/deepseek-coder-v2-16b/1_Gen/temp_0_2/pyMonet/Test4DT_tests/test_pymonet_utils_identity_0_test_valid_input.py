
import pytest
from pymonet.utils import identity  # Assuming this is a hypothetical module

def test_valid_input():
    assert identity(5) == 5
    assert identity("hello") == "hello"
    assert identity([1, 2, 3]) == [1, 2, 3]
    assert identity(True) == True
    assert identity(None) is None
