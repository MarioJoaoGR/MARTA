
import pytest
from ansible.module_utils.splitter import is_quoted

def test_is_quoted_with_double_quotes():
    assert is_quoted("\"Hello, World!\"") == True

def test_is_quoted_with_single_quotes():
    assert is_quoted("'Hello, World!'") == True

def test_is_quoted_empty_string():
    assert is_quoted("") == False

def test_is_quoted_not_enclosed_in_quotes():
    assert is_quoted("Hello, World!") == False
