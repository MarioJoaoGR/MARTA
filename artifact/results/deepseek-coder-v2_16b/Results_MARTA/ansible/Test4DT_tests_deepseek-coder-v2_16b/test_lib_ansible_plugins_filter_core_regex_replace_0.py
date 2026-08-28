
import re
from ansible.plugins.filter.core import regex_replace
import pytest

def test_regex_replace_basic():
    result = regex_replace('Hello World', 'World', 'Universe')
    assert result == 'Hello Universe'

def test_regex_replace_case_insensitive():
    result = regex_replace('Hello World', 'world', 'Universe', ignorecase=True)
    assert result == 'Hello Universe'
