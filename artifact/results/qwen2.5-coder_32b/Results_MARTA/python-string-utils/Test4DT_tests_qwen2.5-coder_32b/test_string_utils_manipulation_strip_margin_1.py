
import pytest
from string_utils.manipulation import strip_margin, InvalidInputError

def test_happy_path():
    input_string = '''\tline 1\n\tline 2\n\tline 3'''
    expected_output = 'line 1\nline 2\nline 3'
    assert strip_margin(input_string) == expected_output

def test_edge_cases():
    # Test with None
    with pytest.raises(InvalidInputError):
        strip_margin(None)
    
    # Test with empty string
    assert strip_margin('') == ''
    
    # Test with single line without tabs
    input_string_single_line_no_tabs = 'single line'
    assert strip_margin(input_string_single_line_no_tabs) == 'single line'

def test_invalid_input_handling():
    # Test with integer
    invalid_int = 123
    with pytest.raises(InvalidInputError):
        strip_margin(invalid_int)
    
    # Test with list
    invalid_list = ['line 1', 'line 2']
    with pytest.raises(InvalidInputError):
        strip_margin(invalid_list)
