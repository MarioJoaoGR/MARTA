
import pytest
from unittest.mock import patch
from ansible.module_utils.common.collections import is_iterable

# Test if a list is considered iterable
def test_valid_case_list():
    with patch('ansible.module_utils.common.collections.is_iterable') as mock_is_iterable:
        mock_is_iterable.return_value = True
        assert is_iterable([1, 2, 3]) == True

# Test if a string is considered iterable with include_strings=True
def test_valid_case_string():
    with patch('ansible.module_utils.common.collections.is_iterable') as mock_is_iterable:
        mock_is_iterable.return_value = True
        assert is_iterable("Hello, World!", include_strings=True) == True

# Test if None is considered not iterable
def test_invalid_case_none():
    with patch('ansible.module_utils.common.collections.is_iterable') as mock_is_iterable:
        mock_is_iterable.return_value = False
        assert is_iterable(None) == False
