
import pytest
from string_utils.manipulation import strip_html

def test_strip_html_basic():
    # Test removing HTML tags completely
    result = strip_html('test: <a href="foo/bar">click here</a>')
    assert result == 'test: '
    
    # Test keeping content within HTML tags
    result_with_content = strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True)
    assert result_with_content == 'test: click here'
