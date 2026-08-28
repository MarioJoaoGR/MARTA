
import pytest
from pysnooper.utils import normalize_repr

# Test valid inputs scenario
def test_valid_inputs():
    class SomeClass:
        def __init__(self):
            self.a = 1
            self.b = 2

        def __repr__(self):
            return "SomeClass(a=1, b=2)"

    obj = SomeClass()
    repr_str = repr(obj)
    clean_repr_str = normalize_repr(repr_str)
    assert clean_repr_str == "SomeClass(a=1, b=2)", f"Expected 'SomeClass(a=1, b=2)', but got {clean_repr_str}"

# Test edge cases scenario
def test_edge_cases():
    obj = "Hello, World!"
    repr_str = repr(obj)
    clean_repr_str = normalize_repr(repr_str)
    assert clean_repr_str == "'Hello, World!'", f"Expected 'Hello, World!', but got {clean_repr_str}"

# Test numeric value scenario
def test_numeric_value():
    obj = 42
    repr_str = repr(obj)
    clean_repr_str = normalize_repr(repr_str)
    assert clean_repr_str == "42", f"Expected '42', but got {clean_repr_str}"
