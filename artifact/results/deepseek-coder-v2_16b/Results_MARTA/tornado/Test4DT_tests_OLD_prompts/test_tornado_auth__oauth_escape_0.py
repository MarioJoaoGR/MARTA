
import pytest
from unittest.mock import patch
import urllib.parse
from typing import Union

# Assuming the function definition provided in the prompt
def _oauth_escape(val: Union[str, bytes]) -> str:
    if isinstance(val, str):
        val = val.encode("utf-8")
    return urllib.parse.quote(val, safe="~")

# Test scenarios

def test_valid_input_string():
    with patch('urllib.parse.quote') as mock_quote:
        mock_quote.return_value = 'Hello%2C+World%21'
        result = _oauth_escape("Hello, World!")
        assert result == 'Hello%2C+World%21'
        mock_quote.assert_called_once_with(b"Hello, World!", safe="~")

def test_valid_input_bytes():
    with patch('urllib.parse.quote') as mock_quote:
        mock_quote.return_value = 'Hello%2C+World%21'
        result = _oauth_escape(b"Hello, World!")
        assert result == 'Hello%2C+World%21'
        mock_quote.assert_called_once_with(b"Hello, World!", safe="~")

def test_invalid_input_none():
    with pytest.raises(TypeError):
        _oauth_escape(None)
