
import pytest
from ansible.parsing.quoting import is_quoted

def test_is_quoted_with_double_quotes():
    assert is_quoted("\"Hello, World!\"") == True

def test_is_quoted_with_single_quotes():
    assert is_quoted('Hello, World!') == False

def test_is_quoted_not_properly_quoted():
    assert is_quoted("'Hello, World!") == False

def test_is_quoted_ends_with_escape_backslash():
    assert is_quoted("\"Hello, World!\\\"") == False
