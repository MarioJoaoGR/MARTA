
import pytest
from unittest.mock import patch
from ansible.plugins.filter.core import regex_findall, to_text


def test_valid_inputs_case_insensitive():
    value = "hello world"
    regex = r"[a-z]+"
    expected = ['hello', 'world']
    with patch('ansible.plugins.filter.core.to_text', return_value=str(value)):
        assert regex_findall(value, regex, ignorecase=True) == expected

def test_valid_inputs_multiline():
    value = "hello\nworld"
    regex = r".+"
    expected = ['hello', 'world']
    with patch('ansible.plugins.filter.core.to_text', return_value=str(value)):
        assert regex_findall(value, regex, multiline=True) == expected


