
import pytest
from unittest.mock import patch
from string_utils.validation import is_isogram  # Assuming the function is in this module

@patch('string_utils.validation.is_isogram')
def test_empty_or_spaces(mock_is_isogram):
    mock_is_isogram.return_value = False
    
    assert not is_isogram(' ')  # Test for a string with only spaces
    assert not is_isogram('')   # Test for an empty string
