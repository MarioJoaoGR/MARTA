
import pytest
from ansible.module_utils.splitter import unquote

def is_quoted(data):
    """ Helper function to check if a string is quoted """
    if len(data) >= 2 and ((data[0] == data[-1]) or (data[0] == '"' and data[-1] == '"') or (data[0] == "'" and data[-1] == "'")):
        return True
    return False

def test_unquote_no_change():
    """ Test unquote function with a string not enclosed in quotes """
    assert unquote("Hello, World!") == "Hello, World!"

def test_unquote_double_quotes():
    """ Test unquote function with a string enclosed in double quotes """
    assert unquote('"Hello, World!"') == "Hello, World!"

def test_unquote_single_quotes():
    """ Test unquote function with a string enclosed in single quotes """
    assert unquote("'Hello, World!'") == 'Hello, World!'

def test_unquote_no_quotes():
    """ Test unquote function with a string not enclosed in any quotes """
    assert unquote("Hello, World!") == "Hello, World!"
