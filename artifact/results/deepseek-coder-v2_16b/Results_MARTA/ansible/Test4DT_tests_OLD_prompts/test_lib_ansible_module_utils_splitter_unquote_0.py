
import pytest
from ansible.module_utils.splitter import unquote, is_quoted
from unittest.mock import patch

def test_unquote_with_no_quotes():
    with patch('ansible.module_utils.splitter.is_quoted', return_value=False):
        result = unquote("Hello, World!")
        assert result == "Hello, World!"

def test_unquote_with_double_quotes():
    with patch('ansible.module_utils.splitter.is_quoted', return_value=True):
        result = unquote('"Hello, World!"')
        assert result == "Hello, World!"

def test_unquote_with_single_quotes():
    with patch('ansible.module_utils.splitter.is_quoted', return_value=True):
        result = unquote("'Hello, World!'")
        assert result == 'Hello, World!'

def test_unquote_with_empty_string():
    with patch('ansible.module_utils.splitter.is_quoted', return_value=False):
        result = unquote("")
        assert result == ""

def test_unquote_with_none():
    with pytest.raises(TypeError):
        unquote(None)
