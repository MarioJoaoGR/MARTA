
import re
from string_utils.validation import InvalidInputError

# Assuming HTML_RE is defined somewhere in your codebase or module
HTML_RE = re.compile(r'<.*?>')

def contains_html(input_string: str) -> bool:
    """
    Checks if the given string contains HTML/XML tags.

    By design, this function matches ANY type of tag, so don't expect to use it as an HTML validator, its goal is to detect "malicious" or undesired tags in the text. It uses a regular expression to detect any occurrence of angle brackets `<` and `>` in the input string, which are typical indicators for HTML or XML tags.

    *Examples:*

    >>> contains_html('my string is <strong>bold</strong>') # returns true
    >>> contains_html('my string is not bold') # returns false

    :param input_string: Text to check for HTML/XML tags.
    :type input_string: str
    :raises InvalidInputError: If the provided `input_string` is not a string, this error will be raised with a descriptive message indicating that the expected type was not met.
    :return: True if the string contains any HTML/XML tags, False otherwise.
    """
    if not isinstance(input_string, str):
        raise InvalidInputError("Expected input to be a string")

    return bool(HTML_RE.search(input_string))

# Test case for invalid input (None)
def test_invalid_input_none():
    with pytest.raises(InvalidInputError):
        contains_html(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_contains_html_2_test_invalid_input_none
python-string-utils/Test4DT_tests/test_string_utils_validation_contains_html_2_test_invalid_input_none.py:31:9: E0602: Undefined variable 'pytest' (undefined-variable)


"""