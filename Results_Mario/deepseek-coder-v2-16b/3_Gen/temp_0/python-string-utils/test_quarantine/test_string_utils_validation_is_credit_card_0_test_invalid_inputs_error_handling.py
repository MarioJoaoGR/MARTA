
import pytest
from string_utils.validation import is_credit_card, CREDIT_CARDS

def test_invalid_inputs_error_handling():
    # Test with an empty string
    assert not is_credit_card('')
    
    # Test with a string of whitespace
    assert not is_credit_card('     ')
    
    # Test with an invalid card type
    with pytest.raises(KeyError) as excinfo:
        is_credit_card('4111 1111 1111 1111', 'INVALID_TYPE')
    assert str(excinfo.value) == 'Invalid card type "INVALID_TYPE". Valid types are: VISA, MASTERCARD, AMERICAN_EXPRESS, DINERS_CLUB, DISCOVER, JCB'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_invalid_inputs_error_handling.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_inputs_error_handling ______________________

    def test_invalid_inputs_error_handling():
        # Test with an empty string
        assert not is_credit_card('')
    
        # Test with a string of whitespace
        assert not is_credit_card('     ')
    
        # Test with an invalid card type
        with pytest.raises(KeyError) as excinfo:
            is_credit_card('4111 1111 1111 1111', 'INVALID_TYPE')
>       assert str(excinfo.value) == 'Invalid card type "INVALID_TYPE". Valid types are: VISA, MASTERCARD, AMERICAN_EXPRESS, DINERS_CLUB, DISCOVER, JCB'
E       assert "'Invalid car...ISCOVER, JCB'" == 'Invalid card...DISCOVER, JCB'
E         
E         - Invalid card type "INVALID_TYPE". Valid types are: VISA, MASTERCARD, AMERICAN_EXPRESS, DINERS_CLUB, DISCOVER, JCB
E         + 'Invalid card type "INVALID_TYPE". Valid types are: VISA, MASTERCARD, AMERICAN_EXPRESS, DINERS_CLUB, DISCOVER, JCB'
E         ? +                                                                                                                 +

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_invalid_inputs_error_handling.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_invalid_inputs_error_handling.py::test_invalid_inputs_error_handling
============================== 1 failed in 0.03s ===============================
"""