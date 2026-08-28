
import pytest
from pysnooper.utils import normalize_repr
import re
from unittest.mock import patch

# Test valid input scenario
def test_valid_input():
    class SomeClass:
        def __init__(self):
            self.a = 1
            self.b = 2

        def __repr__(self):
            return "SomeClass(a=1, b=2)"

    obj = SomeClass()
    repr_str = repr(obj)
    clean_repr_str = normalize_repr(repr_str)
    assert clean_repr_str == "SomeClass(a=1, b=2)"

# Test edge case scenario with None and empty string inputs
def test_edge_case():
    obj = None
    repr_str = repr(obj) if obj else ''
    clean_repr_str = normalize_repr(repr_str)
    assert clean_repr_str == ''

# Test invalid input scenario with non-string representations
def test_invalid_input():
    obj = 42
    repr_str = str(obj)
    with patch('pysnooper.utils.normalize_repr', side_effect=lambda x: str(x)):
        clean_repr_str = normalize_repr(repr_str)
    assert clean_repr_str == "42"
