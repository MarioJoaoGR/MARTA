
import pytest
from unittest.mock import patch
import tornado.escape as escape
import urllib.parse
import sys
import io

# Scenario 1: Test standard input with default behavior (spaces encoded as '+')
def test_valid_input_default_behavior():
    with patch('tornado.escape.urllib.parse.quote_plus', return_value='Hello%2C+World%21'):
        result = escape.url_escape("Hello, World!")
        assert result == 'Hello%2C+World%21'

# Scenario 2: Test standard input with `plus=False` (spaces encoded as '%20')
def test_valid_input_plus_false():
    with patch('tornado.escape.urllib.parse.quote', return_value='Hello%2C%20World%21'):
        result = escape.url_escape("Hello, World!", plus=False)
        assert result == 'Hello%2C%20World%21'

# Scenario 3: Test handling invalid input (None)
def test_invalid_input():
    with pytest.raises(TypeError):
        escape.url_escape(None)
