
import pytest
from string_utils.validation import is_credit_card, CREDIT_CARDS

@pytest.mark.parametrize("card_number", ["3056 9309 0259 04"])
def test_valid_input_diners_club(card_number):
    assert is_credit_card(card_number, 'DINERS_CLUB') == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_diners_club.py F [100%]

=================================== FAILURES ===================================
_______________ test_valid_input_diners_club[3056 9309 0259 04] ________________

card_number = '3056 9309 0259 04'

    @pytest.mark.parametrize("card_number", ["3056 9309 0259 04"])
    def test_valid_input_diners_club(card_number):
>       assert is_credit_card(card_number, 'DINERS_CLUB') == True
E       AssertionError: assert False == True
E        +  where False = is_credit_card('3056 9309 0259 04', 'DINERS_CLUB')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_diners_club.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_diners_club.py::test_valid_input_diners_club[3056 9309 0259 04]
============================== 1 failed in 0.03s ===============================
"""