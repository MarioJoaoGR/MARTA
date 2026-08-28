
import pytest
import re
from ansible.plugins.filter.core import regex_findall


def test_case_insensitive_search():
    result = regex_findall("hello world", r"[a-z]+", ignorecase=True)
    assert result == ['hello', 'world']

def test_multiline_search():
    result = regex_findall("hello\nworld", r".+", multiline=True)
    assert result == ['hello', 'world']


