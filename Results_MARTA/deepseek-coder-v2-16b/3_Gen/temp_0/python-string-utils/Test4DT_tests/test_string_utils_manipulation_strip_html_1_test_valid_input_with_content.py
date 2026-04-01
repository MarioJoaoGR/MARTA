
import re
from string_utils.manipulation import strip_html

def test_valid_input_with_content():
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'
