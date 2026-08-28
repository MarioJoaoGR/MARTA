
import pytest
from ansible.module_utils.splitter import unquote


def test_unquote_empty_string():
    assert unquote('') == ''

def test_unquote_not_quoted():
    assert unquote("Hello, World!") == "Hello, World!"

def test_unquote_double_quotes():
    assert unquote('"Hello, World!"') == 'Hello, World!'

def test_unquote_single_quotes():
    assert unquote("'Hello, World!'") == 'Hello, World!'