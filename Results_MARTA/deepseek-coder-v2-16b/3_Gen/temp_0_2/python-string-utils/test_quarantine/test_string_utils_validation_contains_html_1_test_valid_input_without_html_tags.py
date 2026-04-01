
import re
from string_utils.validation import is_string, InvalidInputError

# Assuming HTML_RE is defined somewhere in a module or imported from a library
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
    if not is_string(input_string):
        raise InvalidInputError(f"Expected a string but got {type(input_string)}")

    return bool(HTML_RE.search(input_string))
```

Now, let's write the test case for `contains_html` function:

```python
import pytest
from unittest.mock import patch
from string_utils.validation import is_string

def test_valid_input_without_html_tags():
    input_string = "my string is not bold"
    assert contains_html(input_string) == False

def test_invalid_input_type():
    with pytest.raises(InvalidInputError):
        contains_html(12345)  # Providing an integer instead of a string

def test_valid_input_with_html_tags():
    input_string = "my string is <strong>bold</strong>"
    assert contains_html(input_string) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_contains_html_1_test_valid_input_without_html_tags
python-string-utils/Test4DT_tests/test_string_utils_validation_contains_html_1_test_valid_input_without_html_tags.py:30:9: E0001: Parsing failed: 'unterminated string literal (detected at line 30) (Test4DT_tests.test_string_utils_validation_contains_html_1_test_valid_input_without_html_tags, line 30)' (syntax-error)


"""