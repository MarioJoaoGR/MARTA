# Module: ansible.plugins.filter.core
# test_ternary.py
import pytest
from ansible.plugins.filter.core import ternary

def test_ternary_true():
    assert ternary(True, 'yes', 'no') == 'yes'

def test_ternary_false():
    assert ternary(False, 'yes', 'no') == 'no'

def test_ternary_none_with_none_val():
    assert ternary(None, 'yes', 'no', 'unknown') == 'unknown'

def test_ternary_non_boolean_value():
    assert ternary('test', 'valid', 'invalid') == 'valid'

# Additional tests for edge cases and potential failures
def test_ternary_none_without_none_val():
    with pytest.raises(TypeError):
        ternary(None, 'yes', 'no')  # Should raise a TypeError as none_val is not provided

def test_ternary_invalid_value_type():
    with pytest.raises(TypeError):
        ternary('invalid type', 'valid', 'invalid')  # Should raise a TypeError as value has an invalid type
