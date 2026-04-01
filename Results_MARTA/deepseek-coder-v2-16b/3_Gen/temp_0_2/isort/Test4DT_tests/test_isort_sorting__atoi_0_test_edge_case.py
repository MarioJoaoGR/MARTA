
import re
from typing import Any

def _natural_keys(text: str) -> list[Any]:
    """
    Converts each character in the input string to its integer representation, using regular expressions to separate digits and non-digits.
    
    Parameters:
        text (str): The input string containing characters that need to be converted to integers.
        
    Returns:
        list[int]: A list of integers obtained by converting each character in the input string to its integer representation, with numeric substrings separated and treated as individual numbers.
    
    Example Usage:
        _natural_keys("a1b2c3") would return [ord('a'), 1, ord('b'), 2, ord('c'), 3] where `ord` is the ASCII value of the character.
    """
    if text is None:
        raise ValueError("Input must not be None")
    
    def _atoi(text: str) -> Any:
        return int(text) if text.isdigit() else text
    
    parts = re.split('([0-9]+)', text)
    result = []
    for part in parts:
        if part.isdigit():
            result.append(_atoi(part))
        elif part:
            result.append(part)
    return result

import pytest

def test_edge_case():
    with pytest.raises(ValueError):
        _natural_keys(None)
