
import pytest
from string_utils import manipulation as sm

def test_strip_html_invalid_input():
    # Test case for invalid input (non-string)
    non_string = 12345
    with pytest.raises(sm.InvalidInputError):
        sm.strip_html(non_string)

def test_strip_html_removes_tags_without_preserving_content():
    input_string = 'test: <a href="foo/bar">click here</a>'
    expected_output = 'test: '
    assert sm.strip_html(input_string) == expected_output

def test_strip_html_preserves_tag_content():
    input_string = 'test: <a href="foo/bar">click here</a>'
    expected_output = 'test: click here'
    assert sm.strip_html(input_string, keep_tag_content=True) == expected_output

def test_strip_html_handles_no_tags():
    input_string = 'this is a plain text without any tags'
    expected_output = 'this is a plain text without any tags'
    assert sm.strip_html(input_string) == expected_output

def test_strip_html_multiple_nested_tags():
    input_string = 'test: <div><b><i>italic bold</i></b></div>'
    expected_output = 'test: '