
import pytest
from unittest.mock import patch
from string_utils.validation import is_pangram

# Test valid pangram input
@patch('string.ascii_lowercase', 'abcdefghijklmnopqrstuvwxyz')
def test_valid_pangram():
    assert is_pangram('The quick brown fox jumps over the lazy dog') == True

# Test invalid pangram input (missing some letters)
@patch('string.ascii_lowercase', 'abcdefghijklmnopqrstuvwxyz')
def test_invalid_pangram():
    assert is_pangram('hello world') == False

# Test empty string
@patch('string.ascii_lowercase', 'abcdefghijklmnopqrstuvwxyz')
def test_empty_string():
    assert is_pangram('') == False

# Test whitespace-only string
@patch('string.ascii_lowercase', 'abcdefghijklmnopqrstuvwxyz')
def test_whitespace_only():
    assert is_pangram(' ') == False
