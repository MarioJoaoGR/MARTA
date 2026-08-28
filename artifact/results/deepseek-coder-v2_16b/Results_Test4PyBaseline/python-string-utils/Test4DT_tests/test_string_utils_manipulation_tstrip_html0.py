
# Module: string_utils.manipulation
import re
from string_utils import manipulation as sm

# Import the function correctly
def test_strip_html_removes_tags_without_preserving_content():
    input_string = 'test: <a href="foo/bar">click here</a>'
    expected_output = 'test: '
    assert sm.strip_html(input_string) == expected_output

def test_strip_html_preserves_tag_content():
    input_string = 'test: <a href="foo/bar">click here</a>'
    expected_output = 'test: click here'