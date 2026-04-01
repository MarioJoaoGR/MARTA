
import re
from string_utils.validation import is_credit_card, CREDIT_CARDS

def test_valid_input_american_express():
    assert is_credit_card('3782 8224 6310 005', 'AMERICAN_EXPRESS') == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_american_express.py F [100%]

=================================== FAILURES ===================================
______________________ test_valid_input_american_express _______________________

    def test_valid_input_american_express():
>       assert is_credit_card('3782 8224 6310 005', 'AMERICAN_EXPRESS') == True
E       AssertionError: assert False == True
E        +  where False = is_credit_card('3782 8224 6310 005', 'AMERICAN_EXPRESS')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_american_express.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_american_express.py::test_valid_input_american_express
============================== 1 failed in 0.04s ===============================
"""