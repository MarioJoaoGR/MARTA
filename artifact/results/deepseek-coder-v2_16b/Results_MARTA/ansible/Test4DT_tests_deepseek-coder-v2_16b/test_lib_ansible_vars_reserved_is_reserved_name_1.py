
import pytest
from ansible.vars.reserved import _RESERVED_NAMES

def is_reserved_name(name):
    return name in _RESERVED_NAMES

# Test for valid input - reserved name

# Test for invalid input - not a reserved name
def test_invalid_input_not_reserved_name():
    assert is_reserved_name("var") == False

# Test for invalid input - None type