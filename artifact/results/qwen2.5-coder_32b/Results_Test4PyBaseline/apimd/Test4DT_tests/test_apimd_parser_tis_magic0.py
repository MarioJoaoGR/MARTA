
import pytest
from apimd.parser import is_magic

def test_is_magic_with_magic_names():
    assert is_magic('__init__') is True, "Test failed for magic method __init__"
    assert is_magic('__str__') is True, "Test failed for magic method __str__"
    assert is_magic('__call__') is True, "Test failed for magic method __call__"

def test_is_magic_with_non_magic_names():
    assert is_magic('my_function') is False, "Test failed for regular function name my_function"
    assert is_magic('_private_method') is False, "Test failed for private method _private_method"