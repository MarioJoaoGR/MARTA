
import re
import pytest
from pysnooper.utils import normalize_repr

# Define the regex pattern used in the function
DEFAULT_REPR_RE = re.compile(r' at 0x[0-9a-fA-F]+>')

def test_normalize_repr_list():
    obj = [1, 2, 3]
    default_repr = repr(obj)
    expected_output = '[1, 2, 3]'
    assert normalize_repr(default_repr) == expected_output

def test_normalize_repr_dict():
    obj = {'key': 'value'}
    default_repr = repr(obj)
    expected_output = "{'key': 'value'}"
    assert normalize_repr(default_repr) == expected_output

def test_normalize_repr_tuple():
    obj = (4, 5, 6)
    default_repr = repr(obj)
    expected_output = '(4, 5, 6)'
    assert normalize_repr(default_repr) == expected_output

def test_normalize_repr_custom_object():
    class CustomObject:
        def __repr__(self):
            return "<CustomObject at 0x123456789>"
    
    obj = CustomObject()
    default_repr = repr(obj)
    expected_output = "<CustomObject>"
    assert normalize_repr(default_repr) == expected_output

def test_normalize_repr_no_memory_address():
    # Test with a string that does not contain a memory address
    item_repr = "This is a test string without memory address"
    expected_output = "This is a test string without memory address"
    assert normalize_repr(item_repr) == expected_output
