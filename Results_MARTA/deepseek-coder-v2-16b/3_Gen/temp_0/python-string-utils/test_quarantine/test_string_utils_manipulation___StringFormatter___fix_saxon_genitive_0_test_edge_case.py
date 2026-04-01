 Sure, here's the pytest function for testing the edge case with `None` input as described:

```python
import pytest
from string_utils.manipulation import is_string, InvalidInputError

class __StringFormatter:
    """
    A class for formatting and validating input strings.

    The `__StringFormatter` class is designed to handle string inputs, ensuring they are valid strings before proceeding with any operations. It raises an `InvalidInputError` if the provided input is not a string.

    Parameters:
        input_string (str): A string that needs to be validated and potentially formatted. This parameter is required for instantiation of the class.

    Raises:
        InvalidInputError: If the provided `input_string` is not a string, this error will be raised with an appropriate message indicating the type of received data.

    Example Usage:
        >>> formatter = __StringFormatter("valid string")
        >>> print(formatter.input_string)  # Outputs: valid string
        
        >>> try:
        ...     bad_formatter = __StringFormatter(12345)  # This will raise InvalidInputError
        ... except InvalidInputError as e:
        ...     print(e)  # Outputs: Expected "str", received "int"
    """
    def __init__(self, input_string):
        if not is_string(input_string):
            raise InvalidInputError(input_string)

        self.input_string = input_string

def test_edge_case():
    with pytest.raises(InvalidInputError) as exc_info:
        formatter = __StringFormatter(None)
    assert str(exc_info.value) == "Expected 'str', received 'NoneType'"
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0_test_edge_case
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0_test_edge_case.py:1:1: E0001: Parsing failed: 'unexpected indent (Test4DT_tests.test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0_test_edge_case, line 1)' (syntax-error)


"""