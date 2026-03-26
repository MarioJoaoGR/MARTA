
import pytest
from string_utils.manipulation import __StringFormatter

def prettify(input_string: str) -> str:
    """
    Reformat a string by applying basic grammar and formatting rules, including capitalization, spacing, and punctuation handling.
    
    The function ensures that the input string adheres to specific stylistic guidelines, such as removing leading or trailing spaces, correcting capitalization after punctuation marks, and ensuring proper spacing around arithmetic operators and special characters like quotes and parentheses. It also handles cases where numbers follow a percentage sign without an intervening space. Additionally, it corrects genitive forms (e.g., "Dave' s dog" to "Dave's dog").
    
    *Examples:*
    
    >>> prettify(' unprettified string ,, like this one,will be"prettified" .it\\\' s awesome! ')
    # -> 'Unprettified string, like this one, will be "prettified". It\'s awesome!'
    
    :param input_string: String to manipulate. Must not be None or empty.
    :return: Prettified string following the specified formatting rules.
    """
    formatted = __StringFormatter(input_string).format()
    return formatted

def test_edge_case_none():
    with pytest.raises(TypeError):
        prettify(None)
