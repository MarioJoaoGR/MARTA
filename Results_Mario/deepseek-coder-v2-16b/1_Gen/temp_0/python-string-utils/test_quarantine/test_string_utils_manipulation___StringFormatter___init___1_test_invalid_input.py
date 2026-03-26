
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
            raise InvalidInputError(f"Expected 'str', received '{type(input_string).__name__}'")

        self.input_string = input_string

def test_invalid_input():
    invalid_input = 12345
    with pytest.raises(InvalidInputError) as excinfo:
        formatter = __StringFormatter(invalid_input)
    assert str(excinfo.value) == "Expected 'str', received 'int'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___init___1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        invalid_input = 12345
        with pytest.raises(InvalidInputError) as excinfo:
            formatter = __StringFormatter(invalid_input)
>       assert str(excinfo.value) == "Expected 'str', received 'int'"
E       assert 'Expected "st...eceived "str"' == "Expected 'st...eceived 'int'"
E         
E         - Expected 'str', received 'int'
E         ?          ^   ^           ^^^ ^
E         + Expected "str", received "str"
E         ?          ^   ^           ^^ ^^

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___init___1_test_invalid_input.py:36: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___init___1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================

"""