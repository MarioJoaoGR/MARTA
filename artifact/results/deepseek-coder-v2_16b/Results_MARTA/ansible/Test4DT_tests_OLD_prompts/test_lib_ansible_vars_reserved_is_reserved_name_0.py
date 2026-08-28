
import pytest
from unittest.mock import patch
from ansible.vars.reserved import _RESERVED_NAMES, is_reserved_name

# Test scenario 1: test_valid_input
def test_valid_input():
    with patch('ansible.vars.reserved._RESERVED_NAMES', {'if', 'print'}):
        assert is_reserved_name("if") == True
        assert is_reserved_name("print") == True
        assert is_reserved_name("var") == False

# Test scenario 2: test_edge_cases
def test_edge_cases():
    with patch('ansible.vars.reserved._RESERVED_NAMES', {'if', 'print'}):
        assert is_reserved_name(None) == False
        assert is_reserved_name("") == False
        assert is_reserved_name(" ") == False
        assert is_reserved_name(123) == False

# Test scenario 3: test_invalid_inputs
def test_invalid_inputs():
    with patch('ansible.vars.reserved._RESERVED_NAMES', {'if', 'print'}):
        with pytest.raises(TypeError):
            is_reserved_name()
