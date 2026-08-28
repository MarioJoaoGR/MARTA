
import pytest
from ansible.plugins.filter.core import ternary

def test_valid_inputs():
    assert ternary(True, 'yes', 'no') == 'yes'

def test_none_case():
    assert ternary(None, 'yes', 'no', none_val='unknown') == 'unknown'

def test_invalid_inputs():
    assert ternary(0, 'yes', 'no') == 'no'
