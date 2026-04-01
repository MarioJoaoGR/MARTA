
import pytest
from string_utils.validation import is_decimal

def test_is_decimal():
    # Test valid decimal numbers
    assert is_decimal('42.0') == True
    assert is_decimal('-123.45e6') == True
    assert is_decimal('+78.9') == True
    
    # Test invalid decimal numbers
    assert is_decimal('123') == False
    assert is_decimal('abc') == False
    assert is_decimal('.') == False
    assert is_decimal('..') == False
    assert is_decimal('42.') == True  # Trailing dot should be valid as per the function logic
    assert is_decimal('-0.0') == True  # Zero with a decimal point should be valid
    assert is_decimal('1e3') == False  # Scientific notation without a following number is invalid

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_is_decimal ________________________________

    def test_is_decimal():
        # Test valid decimal numbers
        assert is_decimal('42.0') == True
        assert is_decimal('-123.45e6') == True
        assert is_decimal('+78.9') == True
    
        # Test invalid decimal numbers
        assert is_decimal('123') == False
        assert is_decimal('abc') == False
        assert is_decimal('.') == False
        assert is_decimal('..') == False
>       assert is_decimal('42.') == True  # Trailing dot should be valid as per the function logic
E       AssertionError: assert False == True
E        +  where False = is_decimal('42.')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_1_test_edge_cases.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_1_test_edge_cases.py::test_is_decimal
============================== 1 failed in 0.03s ===============================

"""