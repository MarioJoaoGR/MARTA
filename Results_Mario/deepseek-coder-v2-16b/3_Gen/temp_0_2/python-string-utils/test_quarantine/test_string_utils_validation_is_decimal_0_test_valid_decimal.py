
import pytest
from string_utils.validation import is_decimal

def test_valid_decimal():
    assert is_decimal('42.0') == True
    assert is_decimal('42') == False
    assert is_decimal('-9.12') == True
    assert is_decimal('1e3') == True
    assert is_decimal('1 2 3') == False
    assert is_decimal('0') == True
    assert is_decimal('.5') == True
    assert is_decimal('-.7') == True
    assert is_decimal('+1.2e-3') == True
    assert is_decimal('abc') == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_0_test_valid_decimal.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_decimal ______________________________

    def test_valid_decimal():
        assert is_decimal('42.0') == True
        assert is_decimal('42') == False
        assert is_decimal('-9.12') == True
>       assert is_decimal('1e3') == True
E       AssertionError: assert False == True
E        +  where False = is_decimal('1e3')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_0_test_valid_decimal.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_0_test_valid_decimal.py::test_valid_decimal
============================== 1 failed in 0.03s ===============================
"""