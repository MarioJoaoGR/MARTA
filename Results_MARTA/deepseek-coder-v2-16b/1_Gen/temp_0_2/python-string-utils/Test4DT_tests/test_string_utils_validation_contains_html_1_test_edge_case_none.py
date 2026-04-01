
import re
import pytest
from string_utils.validation import is_string, InvalidInputError

# Assuming HTML_RE and other imports are correctly set up in string_utils.validation module

def contains_html(input_string: str) -> bool:
    """
    Checks if the given string contains HTML/XML tags.

    By design, this function matches ANY type of tag, so don't expect to use it as an HTML validator, its goal is to detect "malicious" or undesired tags in the text. It uses a regular expression to detect any occurrence of angle brackets `<` and `>` in the input string, which are typical markers for HTML or XML tags.

    *Examples:*

    >>> contains_html('my string is <strong>bold</strong>') # returns true
    >>> contains_html('my string is not bold') # returns false

    :param input_string: Text to check for HTML/XML tags.
    :type input_string: str
    :return: True if the string contains any HTML/XML tags, False otherwise.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    return bool(re.search(r'<[^>]*>', input_string))

def test_edge_case_none():
    with pytest.raises(TypeError):
        contains_html(None)
