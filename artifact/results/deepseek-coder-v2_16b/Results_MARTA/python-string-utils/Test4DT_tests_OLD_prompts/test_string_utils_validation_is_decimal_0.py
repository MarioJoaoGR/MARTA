
import pytest
from string_utils.validation import is_decimal, is_number
from unittest.mock import patch

def test_valid_decimal_numbers():
    with patch('string_utils.validation.is_number', return_value=True):
        assert is_decimal('42.0') == True

def test_invalid_strings():
    with patch('string_utils.validation.is_number', return_value=False):
        assert is_decimal('42') == False

def test_edge_cases():
    with patch('string_utils.validation.is_number', return_value=False):
        assert is_decimal(None) == False
