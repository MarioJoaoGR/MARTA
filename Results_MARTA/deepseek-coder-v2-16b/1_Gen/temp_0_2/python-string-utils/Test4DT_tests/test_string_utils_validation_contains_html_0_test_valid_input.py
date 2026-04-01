
import re
import pytest

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

def test_valid_input():
    # Test case 1: String containing HTML tags
    assert contains_html('my string is <strong>bold</strong>') == True
    
    # Test case 2: String without HTML tags
    assert contains_html('my string is not bold') == False
    
    # Test case 3: Empty string
    assert contains_html('') == False
    
    # Test case 4: String with multiple HTML tags
    assert contains_html('This <span>is</span> a test <em>string</em>.') == True
    
    # Test case 5: String with escaped angle brackets
    assert contains_html('Here are some escaped &lt;tags&gt;.') == False
