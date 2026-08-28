
import pytest
from ansible.plugins.filter.core import strftime
from ansible.errors import AnsibleFilterError
import time

def test_valid_input_happy_path():
    # Test standard input with valid format and optional epoch time
    result = strftime('%Y-%m-%d %H:%M:%S', 1680579296.0)
    assert isinstance(result, str), "Expected a string output"
    assert len(result) == 19, "Expected the length of the string to be 19 characters"

def test_edge_case_none():
    # Test with None as the second parameter
    result = strftime('%Y-%m-%d %H:%M:%S', None)
    assert isinstance(result, str), "Expected a string output"
    assert len(result) == 19, "Expected the length of the string to be 19 characters"

def test_invalid_input_error_handling():
    # Test invalid input for epoch time, expecting AnsibleFilterError
    with pytest.raises(AnsibleFilterError):
        strftime('%Y-%m-%d %H:%M:%S', 'not_a_number')
