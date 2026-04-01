
import re
from string_utils.manipulation import strip_html

def test_valid_input_no_content():
    # Test case where input contains HTML tags but we want to remove them and not preserve the content
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
