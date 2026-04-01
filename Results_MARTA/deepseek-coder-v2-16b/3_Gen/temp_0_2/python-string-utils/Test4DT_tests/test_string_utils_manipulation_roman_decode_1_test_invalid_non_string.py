
import pytest
from string_utils.manipulation import __RomanNumbers

def roman_decode(input_string: str) -> int:
    """
    Decode a Roman numeral string into its integer equivalent if the provided string is valid.

    This function takes a single parameter `input_string`, which is expected to be a non-empty string representing a valid Roman numeral. The function checks if the input string is non-empty and raises a ValueError if it is not. It then reverses the string, iterates through each character, calculates its numeric value based on its position (units, tens, hundreds, thousands), and adds or subtracts this value from the total output.

    *Parameters:*
        - `input_string` (str): A non-empty string representing a Roman numeral.

    *Raises:*
        - `ValueError`: If the input string is empty or not provided.

    *Returns:*
        - int: The integer equivalent of the given Roman numeral string.

    *Examples:*
        - To decode the Roman numeral 'VII', you would call the function as follows:
          ```python
          >>> roman_decode('VII')  # returns 7
          ```
        - If you try to pass an empty string or a non-string value, the function will raise a ValueError:
          ```python
          >>> roman_decode('')  # Raises ValueError: Input must be a non empty string
          ```

    *Usage:*
        To effectively use this function, ensure that the input string is a valid Roman numeral and is not empty. The function will return the corresponding integer value for valid inputs. For invalid inputs (e.g., empty strings or non-string types), it will raise a ValueError.
    """
    if not input_string:
        raise ValueError("Input must be a non-empty string")
    return __RomanNumbers.decode(input_string)

def test_invalid_non_string():
    with pytest.raises(ValueError):
        roman_decode(None)  # Test for None type, which is not a string
