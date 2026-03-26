
import pytest
from string_utils.validation import is_credit_card

def test_valid_input_mastercard():
    input_string = '5500 0000 0000 0004'
    assert is_credit_card(input_string, 'MASTERCARD') == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_mastercard.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_mastercard __________________________

    def test_valid_input_mastercard():
        input_string = '5500 0000 0000 0004'
>       assert is_credit_card(input_string, 'MASTERCARD') == True
E       AssertionError: assert False == True
E        +  where False = is_credit_card('5500 0000 0000 0004', 'MASTERCARD')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_mastercard.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_mastercard.py::test_valid_input_mastercard
============================== 1 failed in 0.03s ===============================
"""