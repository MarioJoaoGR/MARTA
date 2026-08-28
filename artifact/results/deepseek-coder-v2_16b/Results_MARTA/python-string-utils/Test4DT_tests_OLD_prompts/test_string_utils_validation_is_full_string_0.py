
import pytest
from unittest.mock import patch
from string_utils.validation import is_full_string, is_string

def test_is_full_string_none():
    with patch('string_utils.validation.is_string', return_value=False):
        assert is_full_string(None) == False

def test_is_full_string_empty():
    with patch('string_utils.validation.is_string', return_value=False):
        assert is_full_string('') == False

def test_is_full_string_whitespace():
    with patch('string_utils.validation.is_string', return_value=False):
        assert is_full_string(' ') == False

def test_is_full_string_valid():
    with patch('string_utils.validation.is_string', return_value=True):
        assert is_full_string('hello') == True
