
import pytest
from ansible.plugins.filter.urls import unicode_urlencode

def test_valid_input_happy_path():
    string = "Hello World!"
    for_qs = False
    expected_output = 'Hello%20World!'
    assert unicode_urlencode(string, for_qs) == expected_output

def test_edge_case_none():
    string = None
    for_qs = False
    with pytest.raises(TypeError):
        unicode_urlencode(string, for_qs)

def test_invalid_input_error_handling():
    string = 12345
    for_qs = True
    with pytest.raises(TypeError):
        unicode_urlencode(string, for_qs)
