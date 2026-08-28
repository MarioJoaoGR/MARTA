
import pytest
from string_utils.manipulation import strip_margin

def test_strip_margin_with_tabs():
    input_string = '''\tline 1\n\tline 2\n\tline 3'''
    expected_output = 'line 1\nline 2\nline 3'
    assert strip_margin(input_string) == expected_output


def test_strip_margin_single_line_with_tabs():
    input_string = "\tsingle line"
    expected_output = "single line"
    assert strip_margin(input_string) == expected_output

def test_strip_margin_empty_string():
    input_string = ""
    expected_output = ""
    assert strip_margin(input_string) == expected_output

def test_strip_margin_no_leading_tabs():
    input_string = '''line 1\nline 2\nline 3'''
    expected_output = 'line 1\nline 2\nline 3'
    assert strip_margin(input_string) == expected_output