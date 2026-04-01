
import re
import pytest
from string_utils.manipulation import strip_html, InvalidInputError

def test_valid_input_no_content():
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'
