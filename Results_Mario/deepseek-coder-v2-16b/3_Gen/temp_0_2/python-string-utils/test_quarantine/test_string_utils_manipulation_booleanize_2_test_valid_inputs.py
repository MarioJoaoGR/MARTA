
import pytest
from string_utils.manipulation import is_string
from custom_exceptions import InvalidInputError

def booleanize(input_string: str) -> bool:
    """
    Converts a string into a boolean based on its content, in a case-insensitive manner.

    A positive boolean (True) is returned if the string value is one of the following: "true", "1", "yes", or "y". Otherwise, False is returned.

    *Examples:*

    - When you pass the string "true" to the function, it will return `True`:
      ```python
      >>> booleanize('true')  # returns True
      ```

    - When you pass the string "YES", it will also return `True` because the comparison is case-insensitive:
      ```python
      >>> booleanize('YES')  # returns True
      ```

    - If you pass the string "nope", it will return `False`:
      ```python
      >>> booleanize('nope')  # returns False
      ```

    :param input_string: The string to convert.
    :type input_string: str
    :return: True if the string contains a boolean-like positive value, False otherwise.
    """
    if not is_string(input_string):
        raise InvalidInputError(input_string)

    return input_string.lower() in ('true', '1', 'yes', 'y')

def test_valid_inputs():
    # Test cases for valid inputs that should return True
    assert booleanize('true') == True
    assert booleanize('True') == True
    assert booleanize('YES') == True
    assert booleanize('Yes') == True
    assert booleanize('yEs') == True
    assert booleanize('1') == True
    
    # Test cases for valid inputs that should return False
    assert booleanize('false') == False
    assert booleanize('False') == False
    assert booleanize('no') == False
    assert booleanize('No') == False
    assert booleanize('nO') == False
    assert booleanize('0') == False
    
    # Test case for invalid input (should raise InvalidInputError)
    with pytest.raises(InvalidInputError):
        booleanize(123)  # Assuming 123 is not a string and should raise an error

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_booleanize_2_test_valid_inputs
python-string-utils/Test4DT_tests/test_string_utils_manipulation_booleanize_2_test_valid_inputs.py:4:0: E0401: Unable to import 'custom_exceptions' (import-error)


"""