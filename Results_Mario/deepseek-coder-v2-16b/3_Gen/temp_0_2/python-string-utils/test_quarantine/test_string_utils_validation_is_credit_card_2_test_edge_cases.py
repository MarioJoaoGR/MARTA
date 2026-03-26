
import re
from string_utils.validation import CREDIT_CARDS  # Assuming this import exists in your module

def test_edge_cases():
    assert not is_credit_card('')
    assert not is_credit_card('   ')
    assert not is_credit_card('1234567890123456')  # Invalid length
    assert not is_credit_card('4111 1111 1111 1111 invalid')  # Contains non-digit characters
    assert not is_credit_card('3782 8224 6310 005  # Invalid length for American Express
    assert not is_credit_card('3782 8224 6310 005')  # Valid American Express
    assert not is_credit_card('4111 1111 1111 1111')  # Valid VISA
    assert not is_credit_card('5555 5555 5555 4444')  # Valid MasterCard
    assert not is_credit_card('3056 9309 0259 04')   # Invalid Diners Club
    assert not is_credit_card('6011 0009 9013 9424') # Valid Discover
    assert not is_credit_card('3530 1113 3330 0000') # Valid JCB

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_credit_card_2_test_edge_cases
python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_edge_cases.py:10:31: E0001: Parsing failed: 'unterminated string literal (detected at line 10) (Test4DT_tests.test_string_utils_validation_is_credit_card_2_test_edge_cases, line 10)' (syntax-error)


"""