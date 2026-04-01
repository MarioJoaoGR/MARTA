
import re
from string_utils.validation import CREDIT_CARDS

def is_full_string(input_string):
    return bool(re.sub(r'\s+', '', input_string))

def is_credit_card(input_string, card_type=None):
    if not is_full_string(input_string):
        return False

    if card_type:
        if card_type not in CREDIT_CARDS:
            raise KeyError(f'Invalid card type "{card_type}". Valid types are: {", ".join(CREDIT_CARDS.keys())}')
        return bool(re.match(r'^' + CREDIT_CARDS[card_type] + r'$', input_string))

    for c in CREDIT_CARDS:
        if re.match(r'^' + CREDIT_CARDS[c] + r'$', input_string):
            return True

    return False

def test_valid_credit_card_diners_club():
    assert is_credit_card('3782 8224 6310 005', 'DINERS_CLUB') == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_valid_credit_card_diners_club.py F [100%]

=================================== FAILURES ===================================
______________________ test_valid_credit_card_diners_club ______________________

    def test_valid_credit_card_diners_club():
>       assert is_credit_card('3782 8224 6310 005', 'DINERS_CLUB') == True

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_valid_credit_card_diners_club.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_string = '3782 8224 6310 005', card_type = 'DINERS_CLUB'

    def is_credit_card(input_string, card_type=None):
        if not is_full_string(input_string):
            return False
    
        if card_type:
            if card_type not in CREDIT_CARDS:
                raise KeyError(f'Invalid card type "{card_type}". Valid types are: {", ".join(CREDIT_CARDS.keys())}')
>           return bool(re.match(r'^' + CREDIT_CARDS[card_type] + r'$', input_string))
E           TypeError: can only concatenate str (not "re.Pattern") to str

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_valid_credit_card_diners_club.py:15: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_valid_credit_card_diners_club.py::test_valid_credit_card_diners_club
============================== 1 failed in 0.03s ===============================
"""