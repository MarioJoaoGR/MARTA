
import pytest
from ansible.plugins.filter.core import regex_escape
from ansible.errors import AnsibleFilterError
import re

# Helper function to replace characters in a string for posix_basic type
def regex_replace(string, pattern, replacement):
    return re.sub(pattern, replacement, string)

def test_valid_input_python_type():
    result = regex_escape("Hello, World!")
    assert result == "Hello\, World\!", f"Expected 'Hello\, World\!', but got {result}"

def test_valid_input_posix_basic_type():
    result = regex_escape("I am learning regex", re_type='posix_basic')
    expected = "I am learning regex\\.\\^\\$\*\\\\"
    assert result == expected, f"Expected '{expected}', but got {result}"

def test_invalid_input_error_handling():
    with pytest.raises(AnsibleFilterError) as excinfo:
        regex_escape("Example", re_type='posix_extended')
    assert str(excinfo.value) == "Regex type (posix_extended) not yet implemented"
