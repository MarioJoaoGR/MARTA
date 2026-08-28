
import pytest
from unittest.mock import patch
from ansible.module_utils.splitter import is_quoted

def test_valid_input_double_quotes():
    with patch('builtins.print') as mock_print:
        result = is_quoted('"Hello, World!"')
        assert result == True

def test_valid_input_single_quotes():
    with patch('builtins.print') as mock_print:
        result = is_quoted("'Hello, World!'")
        assert result == True

def test_invalid_no_quotes():
    with patch('builtins.print') as mock_print:
        result = is_quoted('Hello, World!')
        assert result == False

def test_empty_string():
    with patch('builtins.print') as mock_print:
        result = is_quoted('')
        assert result == False
