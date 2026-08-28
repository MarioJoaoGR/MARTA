
import pytest
from ansible.plugins.filter.urls import do_urlencode

# Test encoding a valid string input for path component of a URL
def test_valid_string_input():
    value = "Hello World!"
    expected_output = 'Hello%20World!'
    result = do_urlencode(value)
    assert result == expected_output

# Test encoding a dictionary with key-value pairs for query string
def test_valid_dict_input():
    value = {'key': 'value'}
    expected_output = 'key=value'
    result = do_urlencode(value)
    assert result == expected_output

# Test handling invalid non-string, non-dict input
def test_invalid_non_string_input():
    value = 42
    expected_output = '%D1%82%D0%B5%D1%81%D1%82'  # Example output for a Cyrillic string or other binary data
    result = do_urlencode(value)
    assert result == expected_output
