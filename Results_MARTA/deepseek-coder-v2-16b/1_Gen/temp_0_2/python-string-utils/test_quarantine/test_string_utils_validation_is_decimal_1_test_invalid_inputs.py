
import re
import pytest
from string_utils.validation import is_decimal

def test_invalid_inputs():
    # Test cases for invalid inputs
    assert not is_decimal('abc')  # Invalid input should return False
    assert not is_decimal('123abc')  # Invalid input should return False
    assert not is_decimal('12.')  # Invalid input should return False
    assert not is_decimal('.')  # Invalid input should return False
    assert not is_decimal('E-4')  # Invalid input should return False
    assert not is_decimal('-E+4')  # Invalid input should return False
    assert not is_decimal('1.23E')  # Invalid input should return False
    assert not is_decimal('1..23')  # Invalid input should return False
    
    # Test cases for valid inputs
    assert is_decimal('42.0')  # Valid decimal number should return True
    assert is_decimal('42')  # Integer should return False
    assert is_decimal('1.23E-4')  # Valid scientific notation should return True
    assert is_decimal('-1.23E+4')  # Signed and valid scientific notation should return True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test cases for invalid inputs
        assert not is_decimal('abc')  # Invalid input should return False
        assert not is_decimal('123abc')  # Invalid input should return False
        assert not is_decimal('12.')  # Invalid input should return False
        assert not is_decimal('.')  # Invalid input should return False
        assert not is_decimal('E-4')  # Invalid input should return False
        assert not is_decimal('-E+4')  # Invalid input should return False
        assert not is_decimal('1.23E')  # Invalid input should return False
        assert not is_decimal('1..23')  # Invalid input should return False
    
        # Test cases for valid inputs
        assert is_decimal('42.0')  # Valid decimal number should return True
>       assert is_decimal('42')  # Integer should return False
E       AssertionError: assert False
E        +  where False = is_decimal('42')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_1_test_invalid_inputs.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.02s ===============================
"""