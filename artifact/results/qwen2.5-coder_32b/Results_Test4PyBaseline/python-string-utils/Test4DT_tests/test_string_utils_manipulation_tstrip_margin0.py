
# Import the strip_margin function from the appropriate module
from string_utils import strip_margin

def test_strip_margin_with_leading_tabs():
    input_string = '''\tThis is line one.
\t\tThis is line two, indented further.
\tBack to the same level of indentation.'''
    expected_output = '''This is line one.
This is line two, indented further.
Back to the same level of indentation.'''
    assert strip_margin(input_string) == expected_output

def test_strip_margin_without_leading_tabs():
    input_string = '''This is line one.
        This is line two, indented further.
    Back to the same level of indentation.'''
    # The function should return the original string if there are no leading tabs