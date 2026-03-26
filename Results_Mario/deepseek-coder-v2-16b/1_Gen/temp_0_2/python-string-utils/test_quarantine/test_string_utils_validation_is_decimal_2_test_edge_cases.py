
import pytest
from string_utils.validation import is_decimal, is_number

def test_edge_cases():
    # Test None
    with pytest.raises(ValueError):
        assert not is_decimal(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_2_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test None
        with pytest.raises(ValueError):
>           assert not is_decimal(None)

python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_2_test_edge_cases.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
python-string-utils/string_utils/validation.py:172: in is_decimal
    return is_number(input_string) and '.' in input_string
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
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_2_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.03s ===============================
"""