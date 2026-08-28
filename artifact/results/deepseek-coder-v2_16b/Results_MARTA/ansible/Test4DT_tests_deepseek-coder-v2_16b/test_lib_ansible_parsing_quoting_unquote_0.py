
import pytest
from ansible.parsing.quoting import unquote

def is_quoted(data):
    """ Helper function to check if a string is quoted. """
    if len(data) >= 2 and data[0] == data[-1]:
        return True
    return False

def test_unquote_removes_double_quotes():
    assert unquote("\"Hello, World!\"") == "Hello, World!"

def test_unquote_removes_single_quotes():
    assert unquote('\'Hello, World!\'') == "Hello, World!"

def test_unquote_returns_original_if_not_quoted():
    assert unquote("Hello, World!") == "Hello, World!"


def test_unquote_returns_original_if_ends_with_single_quote():
    assert unquote("'Hello, World!") == "'Hello, World!"