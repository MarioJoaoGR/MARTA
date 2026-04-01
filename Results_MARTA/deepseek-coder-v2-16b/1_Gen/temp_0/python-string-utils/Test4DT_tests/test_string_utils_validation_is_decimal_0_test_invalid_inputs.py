
import re
import pytest

def is_decimal(input_string: str) -> bool:
    """
    Checks whether the given string represents a decimal number. A decimal number may be signed or unsigned, and it can include a decimal point followed by digits (optionally with a leading sign). It also supports scientific notation with an 'e' or 'E' followed by an integer.
    
    *Examples:*
    
    >>> is_decimal('42.0') # returns true
    >>> is_decimal('-123.45e6') # returns true
    >>> is_decimal('123') # returns false
    >>> is_decimal('+78.9') # returns true
    >>> is_decimal('abc') # returns false
    
    :param input_string: String to check for whether it represents a decimal number.
    :type input_string: str
    :return: True if the string represents a valid decimal number, False otherwise.
    """
    if not isinstance(input_string, str):
        return False
    
    # Regular expression to match a valid decimal number
    pattern = re.compile(r"""^[-+]?  # Optional sign at the beginning
                               (\d+\.\d* | \.\d+)  # Decimal point followed by digits (optional)
                               ([eE][-+]?\d+)?$  # Scientific notation with optional exponent
                           """, re.VERBOSE)
    return bool(pattern.match(input_string))

# Test invalid inputs
def test_invalid_inputs():
    assert not is_decimal('')
    assert not is_decimal(' ')
    assert not is_decimal(None)
    assert not is_decimal('abc')
    assert not is_decimal('123abc')
    assert not is_decimal('12.34e')
    assert not is_decimal('12.34e+')
    assert not is_decimal('12.34e-')
