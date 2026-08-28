
import pytest
from ansible.plugins.filter.core import ternary

def test_ternary_with_truthy_value():
    result = ternary(True, 'yes', 'no')
    assert result == 'yes'

def test_ternary_with_falsy_value():
    result = ternary(False, 'yes', 'no')
    assert result == 'no'

def test_ternary_with_none_value():
    result = ternary(None, 'yes', 'no', none_val='unknown')
    assert result == 'unknown'

def test_ternary_with_truthy_non_boolean_value():
    result = ternary('hello', 'yes', 'no')
    assert result == 'yes'

def test_ternary_with_falsy_non_boolean_value():
    result = ternary('', 'yes', 'no')
    assert result == 'no'
