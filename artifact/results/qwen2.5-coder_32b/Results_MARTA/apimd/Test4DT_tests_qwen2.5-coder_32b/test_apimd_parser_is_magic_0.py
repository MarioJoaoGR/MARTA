
import pytest
from apimd.parser import is_magic


def test_empty_string():
    """Test that an empty string returns False."""
    assert is_magic('') is False

def test_regular_method_name():
    """Test that a regular method name returns False."""
    assert is_magic('initialize') is False

def test_magic_method_name():
    """Test that a magic method name returns True."""
    assert is_magic('__init__') is True

def test_fully_qualified_magic_method_name():
    """Test that a fully qualified magic method name returns True."""
    assert is_magic('str.__str__') is True

def test_non_magic_start_end():
    """Test that a name starting and ending with '__' but not in the middle returns False."""
    assert is_magic('__main') is False

def test_len_magic_method_name():
    """Test that __len__ method name returns True."""
    assert is_magic('__len__') is True

def test_my_method_name():
    """Test that a non-magic method name returns False."""
    assert is_magic('my_method') is False

def test_doc_magic_method_name():
    """Test that __doc__ method name returns True."""
    assert is_magic('__doc__') is True