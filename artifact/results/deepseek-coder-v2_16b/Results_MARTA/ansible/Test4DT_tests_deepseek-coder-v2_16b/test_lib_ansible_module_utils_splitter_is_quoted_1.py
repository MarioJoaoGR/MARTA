
import pytest
from ansible.module_utils.splitter import is_quoted

# Test case 1: String with double quotes
def test_is_quoted_with_double_quotes():
    assert is_quoted("\"Hello, World!\"") == True

# Test case 2: String with single quotes
def test_is_quoted_with_single_quotes():
    assert is_quoted('\'Hello, World!\'') == True

# Test case 3: Empty string
def test_is_quoted_empty_string():
    assert is_quoted("") == False

# Test case 4: String without quotes
def test_is_quoted_without_quotes():
    assert is_quoted("Hello, World!") == False
