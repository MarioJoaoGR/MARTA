
import pytest
from string_utils.manipulation import __RomanNumbers

def roman_decode(input_string: str) -> int:
    """
    Decode a Roman numeral string into an integer if the provided string is valid.
    
    This function takes a Roman numeral string and converts it to its corresponding integer value. It performs validation checks to ensure that the input string is non-empty and contains only valid Roman numeral characters. If the input string is invalid, it raises a ValueError.
    
    *Examples:*
    
    - Valid conversion:
      ```python
      >>> roman_decode('VII')  # returns 7
      ```
    - Invalid input (None):
      ```python
      >>> roman_decode(None)  # raises ValueError
      ```
    - Invalid input (empty string):
      ```python
      >>> roman_decode('')  # raises ValueError
      ```
    - Invalid input (string with only spaces):
      ```python
      >>> roman_decode(' ')  # raises ValueError
      ```
    
    *Parameters:*
    
    - `input_string` (str): The Roman numeral string to be decoded. It must be a non-empty string containing valid Roman numeral characters.
    
    *Returns:*
    
    - int: The integer value corresponding to the provided Roman numeral string.
    
    *Raises:*
    
    - ValueError: If `input_string` is None, an empty string, or contains only whitespace characters.
    
    *Usage:*
    
    To decode a Roman numeral string, simply call the function with the desired input string:
    
    ```python
    result = roman_decode('VII')  # returns 7
    print(result)  # Output will be 7
    ```
    """
    if not input_string or not isinstance(input_string, str) or input_string.isspace():
        raise ValueError("Invalid input: Input string is empty or invalid.")
    return __RomanNumbers.decode(input_string)

def test_invalid_empty_input():
    with pytest.raises(ValueError):
        roman_decode('')
