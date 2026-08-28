
import pytest
import re
from ansible.plugins.filter.core import regex_escape, to_text, regex_replace, AnsibleFilterError

# Test cases for default usage (Python Regex Type)
def test_regex_escape_default():
    result = regex_escape("Hello, World!")
    assert result == 'Hello\, World\!'

# Test cases for POSIX Basic Regex Type
def test_regex_escape_posix_basic():
    result = regex_escape(".*+?^$[](){}", re_type='posix_basic')
    assert result == '\\.\\*\\+\\?\\^\\$\\[]\\(\\)\\{}\\'

# Test cases for Python Regex Type with special characters
def test_regex_escape_python():
    result = regex_escape("This is a test.")
    assert result == 'This is a test\\.'

# Test cases for invalid regex type
def test_regex_escape_invalid_type():
    with pytest.raises(AnsibleFilterError) as excinfo:
        regex_escape("Example string", re_type='invalid_type')
    assert str(excinfo.value) == 'Invalid regex type (invalid_type)'
