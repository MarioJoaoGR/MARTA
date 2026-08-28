
import pytest
from ansible.plugins.filter import urls
from urllib.parse import unquote_plus

# Assuming PY3 is defined in a way that allows it to be used as expected by the function
PY3 = True  # This should be replaced with actual detection of Python version if needed

def test_unicode_urldecode_valid():
    string = "Hello%20World"
    result = urls.unicode_urldecode(string)
    assert result == unquote_plus(string), f"Expected '{unquote_plus(string)}' but got '{result}'"

