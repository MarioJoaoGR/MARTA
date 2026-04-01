
import pytest
from string_utils.validation import is_credit_card

def test_valid_input_visa():
    assert is_credit_card('4111 1111 1111 1111', 'VISA') == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_visa.py F [100%]

=================================== FAILURES ===================================
____________________________ test_valid_input_visa _____________________________

    def test_valid_input_visa():
>       assert is_credit_card('4111 1111 1111 1111', 'VISA') == True
E       AssertionError: assert False == True
E        +  where False = is_credit_card('4111 1111 1111 1111', 'VISA')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_visa.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_visa.py::test_valid_input_visa
============================== 1 failed in 0.03s ===============================
"""