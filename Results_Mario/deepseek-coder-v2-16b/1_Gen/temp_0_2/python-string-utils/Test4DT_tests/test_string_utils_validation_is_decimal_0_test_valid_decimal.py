
import re
import pytest

def is_decimal(input_string: str) -> bool:
    """
    Checks whether the given string represents a decimal number. A decimal number may be signed or unsigned, and it can include a decimal point followed by one or more digits. It may also be in scientific notation (e.g., 1.23E-4).
    
    Args:
        input_string (str): The string to check for decimal representation.

    Returns:
        bool: True if the string represents a valid decimal number, False otherwise.

    Examples:
        >>> is_decimal('42.0')  # returns True
        >>> is_decimal('42')    # returns False
        >>> is_decimal('1.23E-4')  # returns True
        >>> is_decimal('-1.23E+4')  # returns True
        >>> is_decimal('abc')  # returns False
    """
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    pattern = r'^[+-]?(\d+\.\d*|\.\d+|\d+\.\d+[eE][+-]?\d+)$'
    return bool(re.match(pattern, input_string))

def test_valid_decimal():
    assert is_decimal('42.0') == True
    assert is_decimal('1.23E-4') == True
    assert is_decimal('-1.23E+4') == True
    assert is_decimal('abc') == False
    assert is_decimal('42') == False
