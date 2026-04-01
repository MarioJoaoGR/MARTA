
from string_utils.validation import is_number, InvalidInputError
import re

# Assuming NUMBER_RE is defined somewhere in the validation module
NUMBER_RE = re.compile(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$')

def test_invalid_inputs():
    # Test cases with invalid inputs
    assert not is_number('1 2 3')  # Contains spaces
    assert not is_number('abc')    # Not a number
    assert not is_number('1a2b3c') # Contains alphabets
    assert not is_number('')       # Empty string
    assert not is_number(' ')      # Whitespace only
    assert not is_number(None)     # None type

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_number_5_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test cases with invalid inputs
        assert not is_number('1 2 3')  # Contains spaces
        assert not is_number('abc')    # Not a number
        assert not is_number('1a2b3c') # Contains alphabets
        assert not is_number('')       # Empty string
        assert not is_number(' ')      # Whitespace only
>       assert not is_number(None)     # None type

python-string-utils/Test4DT_tests/test_string_utils_validation_is_number_5_test_invalid_inputs.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_string = None

    def is_number(input_string: str) -> bool:
        """
        Checks if a string is a valid number.
    
        The number can be a signed (eg: +1, -2, -3.3) or unsigned (eg: 1, 2, 3.3) integer or double
        or use the "scientific notation" (eg: 1e5).
    
        *Examples:*
    
        >>> is_number('42') # returns true
        >>> is_number('19.99') # returns true
        >>> is_number('-9.12') # returns true
        >>> is_number('1e3') # returns true
        >>> is_number('1 2 3') # returns false
    
        :param input_string: String to check
        :type input_string: str
        :return: True if the string represents a number, false otherwise
        """
        if not isinstance(input_string, str):
>           raise InvalidInputError(input_string)
E           string_utils.errors.InvalidInputError: Expected "str", received "NoneType"

python-string-utils/string_utils/validation.py:136: InvalidInputError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_number_5_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.04s ===============================
"""