
import re
from string_utils.manipulation import strip_html

def test_valid_input_with_content():
    # Test case 1: Removing HTML tags without preserving content
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
    
    # Test case 2: Preserving the content of HTML tags
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'
