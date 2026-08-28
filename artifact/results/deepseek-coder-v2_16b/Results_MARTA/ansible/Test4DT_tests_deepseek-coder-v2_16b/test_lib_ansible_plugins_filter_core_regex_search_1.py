
import pytest
from ansible.plugins.filter.core import regex_search
from ansible.errors import AnsibleFilterError

def test_regex_search_basic():
    result = regex_search('hello world', r'world')
    assert result == 'world'

def test_regex_search_case_insensitive():
    result = regex_search('Hello World', r'world', ignorecase=True)
    assert result == 'World'


