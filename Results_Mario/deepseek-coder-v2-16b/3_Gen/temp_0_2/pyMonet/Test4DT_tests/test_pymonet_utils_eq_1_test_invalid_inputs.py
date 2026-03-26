
import pytest
from pymonet.utils import eq  # Assuming this is a hypothetical module with the eq function

def test_invalid_inputs():
    # Test cases for invalid inputs
    assert not eq(5, "5")  # Different types (int vs str)
    assert not eq("hello", "world")  # Different values
    assert not eq([1, 2], [3, 4])  # Different lists
    assert not eq(None, False)  # None vs boolean
    assert not eq("", [])  # Empty string vs empty list
