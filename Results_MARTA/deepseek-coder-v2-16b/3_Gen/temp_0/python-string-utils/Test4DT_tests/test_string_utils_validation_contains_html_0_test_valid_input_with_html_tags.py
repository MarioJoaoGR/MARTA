
import re
from string_utils.validation import contains_html

def test_valid_input_with_html_tags():
    assert contains_html('my string is <strong>bold</strong>') == True
    assert contains_html('my string is not bold') == False
