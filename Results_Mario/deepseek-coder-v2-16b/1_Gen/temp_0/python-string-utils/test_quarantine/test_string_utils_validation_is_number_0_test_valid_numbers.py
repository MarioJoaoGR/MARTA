
import re
from string_utils.validation import is_number, InvalidInputError

# Define the regular expression for matching numbers
NUMBER_RE = re.compile(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$')

def test_valid_numbers():
    # Test cases for valid numbers
    assert is_number('42') == True
    assert is_number('19.99') == True
    assert is_number('-9.12') == True
    assert is_number('1e3') == True
    assert is_number('+1e-5') == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_number_0_test_valid_numbers.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_numbers ______________________________

    def test_valid_numbers():
        # Test cases for valid numbers
        assert is_number('42') == True
        assert is_number('19.99') == True
        assert is_number('-9.12') == True
        assert is_number('1e3') == True
>       assert is_number('+1e-5') == True
E       AssertionError: assert False == True
E        +  where False = is_number('+1e-5')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_number_0_test_valid_numbers.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_number_0_test_valid_numbers.py::test_valid_numbers
============================== 1 failed in 0.02s ===============================

"""