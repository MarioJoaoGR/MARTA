
import pytest
from unittest.mock import patch
from string_utils.validation import is_isbn

# Test valid ISBN-10 number

# Test valid ISBN-13 number
def test_valid_isbn_13():
    with patch('string_utils.validation.__ISBNChecker', autospec=True) as mock_checker:
        mock_instance = mock_checker.return_value
        mock_instance.is_isbn_13.return_value = True
        assert is_isbn('9780312498580') == True

# Test invalid ISBN number with hyphens and normalization enabled
def test_invalid_isbn_with_hyphens():
    with patch('string_utils.validation.__ISBNChecker', autospec=True) as mock_checker:
        mock_instance = mock_checker.return_value
        mock_instance.is_isbn_13.return_value = False
        mock_instance.is_isbn_10.return_value = False
        assert is_isbn('978-0-312-49858-0') == False

# Test valid ISBN number with normalization disabled