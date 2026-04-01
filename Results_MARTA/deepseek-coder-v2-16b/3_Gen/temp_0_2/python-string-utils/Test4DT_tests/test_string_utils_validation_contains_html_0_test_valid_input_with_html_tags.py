
import pytest
from string_utils.validation import contains_html

def test_valid_input_with_html_tags():
    input_string = 'my string is <strong>bold</strong>'
    assert contains_html(input_string) == True

def test_invalid_input_without_html_tags():
    input_string = 'my string is not bold'
    assert contains_html(input_string) == False
