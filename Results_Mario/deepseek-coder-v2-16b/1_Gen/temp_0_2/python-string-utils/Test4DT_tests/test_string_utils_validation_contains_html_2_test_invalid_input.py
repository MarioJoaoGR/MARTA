
import re
import pytest
from string_utils.validation import is_string, InvalidInputError

def contains_html(input_string: str) -> bool:
    """
    Checks if the given string contains HTML/XML tags.

    By design, this function matches ANY type of tag, so don't expect to use it
    as an HTML validator, its goal is to detect "malicious" or undesired tags in the text.

    *Examples:*

    >>> contains_html('my string is <strong>bold</strong>') # returns true
    >>> contains_html('my string is not bold') # returns false

    :param input_string: Text to check
    :type input_string: str
    :return: True if string contains html, false otherwise.
    """
    if not is_string(input_string):
        raise InvalidInputError(input_string)

    return HTML_RE.search(input_string) is not None

# Assuming HTML_RE is defined somewhere in the module or imported from a library
HTML_RE = re.compile(r'<[^>]*>', re.IGNORECASE)

def test_invalid_input():
    with pytest.raises(TypeError):
        contains_html(12345)  # An integer input should raise TypeError
    with pytest.raises(TypeError):
        contains_html(['this', 'is', 'a', 'list'])  # A list input should raise TypeError
