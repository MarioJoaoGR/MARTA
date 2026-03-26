
import re
from string_utils.validation import contains_html

def test_valid_input_without_html_tags():
    # Test case where input string does not contain HTML tags
    input_string = "my string is not bold"
    assert not contains_html(input_string), f"Expected False for input: {input_string}"
