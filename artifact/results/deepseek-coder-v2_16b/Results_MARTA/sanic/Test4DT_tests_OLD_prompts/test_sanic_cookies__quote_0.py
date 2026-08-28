
import pytest
from sanic import Sanic
from sanic.cookies import _quote, _is_legal_key
from unittest.mock import patch

# Test for valid input strings that do not need quoting

# Test for edge cases including None, empty string, and strings with special characters

# Additional tests to ensure the function handles all edge cases correctly

def test_none_input():
    assert _quote(None) is None

def test_empty_string():
    assert _quote("") == '""'