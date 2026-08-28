
import re
import pytest

# Define the regex pattern used in the function
DEFAULT_REPR_RE = re.compile(r' at 0x[0-9a-fA-F]+>')

def normalize_repr(item_repr):
    """Remove memory address (0x...) from a default python repr"""
    return DEFAULT_REPR_RE.sub('', item_repr)

# Test cases

def test_valid_case():
    obj1 = [1, 2, 3]
    obj2 = {'key': 'value'}
    obj3 = (4, 5, 6)
    
    assert normalize_repr(repr(obj1)) == '[1, 2, 3]'
    assert normalize_repr(repr(obj2)) == "{'key': 'value'}"
    assert normalize_repr(repr(obj3)) == '(4, 5, 6)'

def test_edge_case():
    obj1 = None
    obj2 = []
    obj3 = ''
    
    assert normalize_repr(repr(obj1)) == 'None'
    assert normalize_repr(repr(obj2)) == '[]'
    assert normalize_repr(repr(obj3)) == "''"

def test_invalid_input():
    obj1 = 12345
    obj2 = True
    obj3 = [None]
    
    assert normalize_repr(repr(obj1)) == '12345'
    assert normalize_repr(repr(obj2)) == 'True'
    assert normalize_repr(repr(obj3)) == '[None]'
