
import pytest
from ansible.vars.reserved import is_reserved_name, _RESERVED_NAMES

# Test scenario 1: test_valid_input
def test_valid_input():
    assert is_reserved_name("if") == True
    assert is_reserved_name("print") == True
    assert is_reserved_name("var") == False

# Test scenario 2: test_edge_case_none
def test_edge_case_none():
    with pytest.raises(TypeError):
        is_reserved_name(None)

# Test scenario 3: test_invalid_input
def test_invalid_input():
    assert is_reserved_name("if") == True
    assert is_reserved_name("print") == True
    assert is_reserved_name("var") == False
