
import pytest
from unittest.mock import patch
from string_utils.validation import is_credit_card, CREDIT_CARDS

# Test valid VISA card number

# Test valid American Express card number

# Test invalid card number format
def test_invalid_credit_card():
    with patch('string_utils.validation.is_full_string', return_value=True):
        assert is_credit_card('1234-5678-9012-3456') == False

# Test empty string input
def test_empty_input():
    with patch('string_utils.validation.is_full_string', return_value=False):
        assert is_credit_card('') == False

# Test whitespace only input
def test_whitespace_only():
    with patch('string_utils.validation.is_full_string', return_value=False):
        assert is_credit_card('   ') == False