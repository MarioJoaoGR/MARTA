
import pytest
from string_utils.manipulation import __StringFormatter

def prettify(input_string: str) -> str:
    """
    Reformat a string by applying basic grammar and formatting rules to ensure it is clean, well-structured, and follows common conventions. The function ensures that the first letter of each sentence is uppercase, removes multiple sequential spaces, enforces proper spacing around punctuation marks, corrects Saxon genitive cases, and ensures consistent spacing on both sides of specific characters such as quotes and parentheses. It also handles arithmetic operators and adjusts spacing based on their usage.

    *Examples:*

    >>> prettify(' unprettified string ,, like this one,will be"prettified" .it\\' s awesome! ')
    # -> 'Unprettified string, like this one, will be "prettified". It\'s awesome!'

    Parameters:
        input_string (str): The string to be prettified. This should not include leading or trailing spaces and should follow the specified rules for proper formatting.
        
    Returns:
        str: The prettified string after applying all the formatting rules.
    """
    formatted = __StringFormatter(input_string).format()
    return formatted

# Test cases
def test_valid_input():
    input_string = ' unprettified string ,, like this one,will be"prettified" .it\' s awesome! '
    expected_output = 'Unprettified string, like this one, will be "prettified". It\'s awesome!'
    assert prettify(input_string) == expected_output

def test_edge_case():
    input_string = ''
    expected_output = ''
    assert prettify(input_string) == expected_output

def test_invalid_input():
    with pytest.raises(TypeError):
        prettify(None)
