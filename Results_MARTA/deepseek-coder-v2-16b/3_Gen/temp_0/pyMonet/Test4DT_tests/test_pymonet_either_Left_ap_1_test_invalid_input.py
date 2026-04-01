
import pytest
from pymonet.either import Left, Right  # Assuming pymonet is a module with Either implementation

def test_invalid_input():
    try:
        left_invalid = Left([])  # Invalid input type should raise TypeError
    except TypeError as e:
        assert str(e) == "Expected a value of type A, but got list"
