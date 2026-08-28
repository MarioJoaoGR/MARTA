
import pytest
from ansible.plugins.filter.core import ternary

def test_ternary_true():
    assert ternary(True, 'yes', 'no') == 'yes'

def test_ternary_false():
    assert ternary(False, 'yes', 'no') == 'no'

def test_ternary_none_with_none_val():
    assert ternary(None, 'yes', 'no', none_val='unknown') == 'unknown'

def test_ternary_truthy_value():
    assert ternary('hello', 'yes', 'no') == 'yes'

def test_ternary_falsy_value():
    assert ternary('', 'yes', 'no') == 'no'
