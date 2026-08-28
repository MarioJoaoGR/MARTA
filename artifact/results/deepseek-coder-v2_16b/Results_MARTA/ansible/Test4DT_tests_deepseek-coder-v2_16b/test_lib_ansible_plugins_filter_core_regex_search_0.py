
import pytest
from ansible.plugins.filter.core import regex_search

def test_regex_search_basic():
    # Test basic functionality without any additional arguments
    result = regex_search('hello world', r'world')
    assert result == 'world'

    # Test case-insensitive search
    result = regex_search('Hello World', r'world', ignorecase=True)
    assert result == 'World'

