
import pytest
from unittest.mock import patch
from ansible.utils.vars import _isidentifier_PY2

def test_valid_identifier():
    with patch('ansible.utils.vars._isidentifier_PY2', return_value=True):
        ident = 'my_variable'
        assert _isidentifier_PY2(ident) is True

def test_invalid_start_with_digit():
    with patch('ansible.utils.vars._isidentifier_PY2', return_value=False):
        ident = '123abc'
        assert _isidentifier_PY2(ident) is False

def test_empty_string():
    with patch('ansible.utils.vars._isidentifier_PY2', return_value=False):
        ident = ''
        assert _isidentifier_PY2(ident) is False
