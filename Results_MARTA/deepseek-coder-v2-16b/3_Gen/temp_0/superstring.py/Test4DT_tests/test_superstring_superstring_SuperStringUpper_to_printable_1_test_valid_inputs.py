
import pytest
from superstring.superstring import SuperString

class SuperStringUpper:
    """
    Converts a portion of the stored string to uppercase using the `SuperStringUpper` class.

    Parameters:
        base (SuperString): The initial string content to be stored in the SuperString instance from which the substring will be extracted.

    Methods:
        to_printable(start_index=None, end_index=None): Returns a printable representation of the substring converted to uppercase. If start_index and/or end_index are provided, it returns an uppercase substring from start_index to end_index.
            Parameters:
                start_index (int, optional): The starting index for the substring that should be converted to uppercase. Defaults to None, which means the conversion will apply to the entire string if not specified otherwise.
                end_index (int, optional): The ending index for the substring that should be converted to uppercase. Defaults to None, which means the conversion will apply to the entire string if start_index is not provided.
            Returns:
                str: A new string with the specified portion(s) converted to uppercase. If both `start_index` and `end_index` are provided, it returns a substring from `start_index` to `end_index` in uppercase. If only one of them is provided, it converts the entire string up to that index to uppercase.

    Example Usage:
        >>> s = SuperStringUpper(SuperString("Hello, World!"))
        >>> print(s.to_printable())  # Output will be "HELLO, WORLD!"
        >>> print(s.to_printable(7, 12))  # Output will be "WORLD"
        >>> print(s.to_printable(None, None))  # Equivalent to s.to_printable(), output will be "HELLO, WORLD!"
        >>> print(s.to_printable(7, None))  # Output will be "WORLD!"
        >>> print(s.to_printable(None, 5))  # Output will be "HELLO"
    """
    def __init__(self, base):
        self._base = base

    def to_printable(self, start_index=None, end_index=None):
        return self._base.to_printable(start_index, end_index).upper()

def test_valid_inputs():
    s = SuperStringUpper(SuperString("Hello, World!"))
    
    # Test with default parameters (entire string)
    assert s.to_printable() == "HELLO, WORLD!"
    
    # Test with specified start and end indices
    assert s.to_printable(7, 12) == "WORLD"
    
    # Test with only start index provided
    assert s.to_printable(None, None) == "HELLO, WORLD!"
    
    # Test with only end index provided
    assert s.to_printable(7, None) == "WORLD!"
    
    # Test with only start index provided
    assert s.to_printable(None, 5) == "HELLO"
