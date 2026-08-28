
import pytest
from collections import defaultdict
from ansible.plugins.lookup.ini import _parse_params

# Test cases for _parse_params function

def test_basic_usage():
    term = 'name=John age=30'
    paramvals = {'name': 'default_name', 'age': 25}
    result = _parse_params(term, paramvals)
    assert result == ['John', '30']

def test_multiple_terms():
    term = 'John 30'
    paramvals = {'name': 'default_name', 'age': 25}
    result = _parse_params(term, paramvals)
    assert result == ['', '', '30']

def test_using_default_values():
    term = 'John'
    paramvals = {'name': 'default_name', 'age': 25}
    result = _parse_params(term, paramvals)
    assert result == ['default_name', '']

def test_handling_no_terms():
    term = ''
    paramvals = {'name': 'default_name', 'age': 25}
    result = _parse_params(term, paramvals)
    assert result == ['', '', '']

def test_invalid_key():
    term = 'name=John age=30 key=extra'
    paramvals = {'name': 'default_name', 'age': 25}
    result = _parse_params(term, paramvals)
    assert result == ['John', '30']

def test_empty_paramvals():
    term = 'name=John age=30'
    paramvals = {}
    result = _parse_params(term, paramvals)
    assert result == ['John', '30']

def test_none_term():
    term = None
    paramvals = {'name': 'default_name', 'age': 25}
    with pytest.raises(TypeError):
        _parse_params(term, paramvals)

def test_none_paramvals():
    term = 'name=John age=30'
    paramvals = None
    with pytest.raises(TypeError):
        _parse_params(term, paramvals)
