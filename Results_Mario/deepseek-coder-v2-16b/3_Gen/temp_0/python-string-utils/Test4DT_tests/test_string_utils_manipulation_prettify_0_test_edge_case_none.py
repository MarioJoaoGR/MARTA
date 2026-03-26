
import pytest
from string_utils.manipulation import __StringFormatter

def prettify(input_string: str) -> str:
    """
    Reformat a string by applying basic grammar and formatting rules, including capitalization of the first letter after certain punctuation marks, spacing around quotes and brackets, and ensuring proper handling of arithmetic operators.

    This function ensures that the input string adheres to specific rules for spacing, capitalization, and punctuation. It also handles special cases such as arithmetic operators, quoted text, bracketed text, and percentage signs when preceded by numbers.

    *Examples:*

    >>> prettify(' unprettified string ,, like this one,will be"prettified" .it\\' s awesome! ')
    'Unprettified string, like this one, will be "prettified". It\'s awesome!'

    :param input_string: A string that needs to be manipulated according to specified rules.
    :return: The prettified string following the applied formatting rules.
    """
    formatted = __StringFormatter(input_string).format()
    return formatted

def test_edge_case_none():
    with pytest.raises(TypeError):
        prettify(None)
