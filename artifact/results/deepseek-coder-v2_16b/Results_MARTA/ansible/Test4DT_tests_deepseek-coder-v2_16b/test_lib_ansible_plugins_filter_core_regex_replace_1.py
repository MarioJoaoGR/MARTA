
import pytest
from ansible.plugins.filter.core import regex_replace
import re

def to_text(value, errors='surrogate_or_strict', nonstring='simplerepr'):
    if value is None:
        return ''
    elif isinstance(value, bytes):
        try:
            return value.decode('utf-8')
        except UnicodeDecodeError:
            return value.decode('latin1')
    else:
        return str(value)

# Test scenarios
def test_valid_inputs():
    result = regex_replace('Hello World', 'World', 'Universe')
    assert result == 'Hello Universe'

def test_edge_cases():
    # None input
    with pytest.raises(TypeError):
        regex_replace(None, '', '')
    
    # Empty string input
    assert regex_replace('', '', '') == ''
    
    # Boundary values for pattern and replacement
    assert regex_replace('Hello World', '', 'Universe') == 'Hello World'
    assert regex_replace('Hello World', 'Hello', '') == ' World'

def test_invalid_inputs():
    with pytest.raises(TypeError):
        regex_replace(123, 456, 789)
    
    with pytest.raises(TypeError):
        regex_replace('Hello World', None, 'Universe')
    
    with pytest.raises(TypeError):
        regex_replace('Hello World', 'World', None)
