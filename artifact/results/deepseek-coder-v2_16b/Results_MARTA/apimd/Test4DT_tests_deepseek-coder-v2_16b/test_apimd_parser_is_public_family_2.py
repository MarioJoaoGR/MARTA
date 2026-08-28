
import pytest
from apimd.parser import is_public_family

# Test cases for public module names
def test_valid_case_simple_public():
    assert is_public_family('os') == True

def test_valid_case_hierarchical_public():
    assert is_public_family('os.path') == True

# Test cases for private module names
def test_invalid_case_private():
    assert is_public_family('sys._abc') == False

def test_invalid_case_local():
    assert is_public_family('_collections') == False

# Edge cases
def test_edge_case_none():
    with pytest.raises(AttributeError):
        is_public_family(None)

def test_edge_case_empty_string():
    assert is_public_family('') == True
