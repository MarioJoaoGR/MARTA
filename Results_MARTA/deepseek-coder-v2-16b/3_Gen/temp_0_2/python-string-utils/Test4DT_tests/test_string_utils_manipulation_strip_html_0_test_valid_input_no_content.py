
import re
from string_utils.manipulation import strip_html
import pytest

def test_valid_input_no_content():
    # Test case where HTML tags are removed and their content is not preserved
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
