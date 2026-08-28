
import pytest
import re

# Define the regex pattern for removing memory addresses in repr strings
DEFAULT_REPR_RE = re.compile(r'<[^>]+object at 0x[a-fA-F0-9]+>')

def normalize_repr(item_repr):
    """Remove memory address (0x...) from a default python repr"""
    return DEFAULT_REPR_RE.sub('', item_repr)

# Test cases
class SomeClass:
    def __init__(self):
        self.a = 1
        self.b = 2
    def __repr__(self):
        return "SomeClass(a=1, b=2)"

@pytest.fixture
def some_instance():
    return SomeClass()

# Test valid case with a custom class instance
def test_valid_case_1(some_instance):
    repr_str = repr(some_instance)
    clean_repr_str = normalize_repr(repr_str)
    assert clean_repr_str == "SomeClass(a=1, b=2)"

# Test valid case with a string representation
def test_valid_case_2():
    obj = 'Hello, World!'
    repr_str = repr(obj)
    clean_repr_str = normalize_repr(repr_str)
    assert clean_repr_str == "'Hello, World!'"

# Test valid case with a numeric value
def test_valid_case_3():
    obj = 42
    repr_str = repr(obj)
    clean_repr_str = normalize_repr(repr_str)
    assert clean_repr_str == "42"

# Test edge case with None input
def test_edge_case_1():
    item_repr = None
    with pytest.raises(TypeError):
        normalize_repr(item_repr)

# Test edge case with empty string input
def test_edge_case_2():
    item_repr = ''
    clean_repr_str = normalize_repr(item_repr)
    assert clean_repr_str == ''

# Test error case for non-string input
def test_error_case_1():
    item_repr = 123
    with pytest.raises(TypeError):
        normalize_repr(item_repr)
