# Module: ansible.plugins.filter.core
import pytest
from ansible.plugins.filter.core import to_bool

# Test cases for the to_bool function
def test_to_bool_none():
    assert not to_bool(None)  # Output should be False

def test_to_bool_true_boolean():
    assert to_bool(True)  # Output should be True

def test_to_bool_truthy_string():
    assert to_bool('Yes')  # Output should be True

def test_to_bool_falsy_string():
    assert not to_bool('NO')  # Output should be False

def test_to_bool_truthy_numeric_string():
    assert to_bool('1')  # Output should be True

def test_to_bool_falsy_numeric_string():
    assert not to_bool('0')  # Output should be False
