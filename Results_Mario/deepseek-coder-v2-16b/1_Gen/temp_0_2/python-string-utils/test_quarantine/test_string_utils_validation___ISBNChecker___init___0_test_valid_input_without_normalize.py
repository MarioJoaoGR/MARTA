
import pytest
from string_utils.errors import InvalidInputError
from string_utils.validation import is_string

class __ISBNChecker:
    def __init__(self, input_string: str, normalize: bool = True):
        if not is_string(input_string):
            raise InvalidInputError(f"Expected 'str', received {type(input_string).__name__}")

        self.input_string = input_string.replace('-', '') if normalize else input_string

def test_valid_input_without_normalize():
    # Arrange
    input_string = "9783161484100"
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        __ISBNChecker(input_string)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___0_test_valid_input_without_normalize.py F [100%]

=================================== FAILURES ===================================
______________________ test_valid_input_without_normalize ______________________

    def test_valid_input_without_normalize():
        # Arrange
        input_string = "9783161484100"
    
        # Act & Assert
>       with pytest.raises(InvalidInputError):
E       Failed: DID NOT RAISE <class 'string_utils.errors.InvalidInputError'>

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___0_test_valid_input_without_normalize.py:18: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___0_test_valid_input_without_normalize.py::test_valid_input_without_normalize
============================== 1 failed in 0.03s ===============================
"""