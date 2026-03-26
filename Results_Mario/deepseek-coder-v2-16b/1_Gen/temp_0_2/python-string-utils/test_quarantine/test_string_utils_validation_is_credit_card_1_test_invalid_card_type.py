
import pytest
from string_utils.validation import is_credit_card, CREDIT_CARDS

def test_invalid_card_type():
    input_string = '4532790782910562'
    card_type = 'INVALID'
    
    with pytest.raises(KeyError) as excinfo:
        is_credit_card(input_string, card_type)
    
    assert str(excinfo.value) == f'Invalid card type "{card_type}". Valid types are: {", ".join(CREDIT_CARDS.keys())}'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_1_test_invalid_card_type.py F [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_card_type ____________________________

    def test_invalid_card_type():
        input_string = '4532790782910562'
        card_type = 'INVALID'
    
        with pytest.raises(KeyError) as excinfo:
            is_credit_card(input_string, card_type)
    
>       assert str(excinfo.value) == f'Invalid card type "{card_type}". Valid types are: {", ".join(CREDIT_CARDS.keys())}'
E       assert "'Invalid car...ISCOVER, JCB'" == 'Invalid card...DISCOVER, JCB'
E         
E         - Invalid card type "INVALID". Valid types are: VISA, MASTERCARD, AMERICAN_EXPRESS, DINERS_CLUB, DISCOVER, JCB
E         + 'Invalid card type "INVALID". Valid types are: VISA, MASTERCARD, AMERICAN_EXPRESS, DINERS_CLUB, DISCOVER, JCB'
E         ? +                                                                                                            +

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_1_test_invalid_card_type.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_1_test_invalid_card_type.py::test_invalid_card_type
============================== 1 failed in 0.04s ===============================
"""