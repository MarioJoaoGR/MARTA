
import pytest
from string_utils.validation import is_credit_card
import re

# Define a dictionary of known credit card patterns
CREDIT_CARDS = {
    'VISA': re.compile(r'^4[0-9]{12}(?:[0-9]{3})?$'),
    'MASTERCARD': re.compile(r'^5[1-5][0-9]{14}$'),
    'AMERICAN_EXPRESS': re.compile(r'^3(?:4|7)[0-9]{13}$'),
    'DINERS_CLUB': re.compile(r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$'),
    'DISCOVER': re.compile(r'^6(?:011|5[0-9]{2})[0-9]{12}$'),
    'JCB': re.compile(r'^(?:2131|1800)[0-9]{11}$')
}

def test_invalid_inputs_error_handling():
    # Test with invalid card type
    with pytest.raises(KeyError):
        is_credit_card('4111 1111 1111 1111', 'INVALID_TYPE')
    
    # Test with empty string
    assert not is_credit_card('')
    
    # Test with non-numeric characters
    assert not is_credit_card('invalid input')
    
    # Test with valid VISA card
    assert is_credit_card('4111 1111 1111 1111', 'VISA')
    
    # Test with valid MasterCard
    assert is_credit_card('5105 1051 0510 5100', 'MASTERCARD')
    
    # Test with valid American Express
    assert is_credit_card('3782 822463 10005', 'AMERICAN_EXPRESS')
    
    # Test with valid Diners Club
    assert not is_credit_card('30569309025904', 'DINERS_CLUB')
    
    # Test with valid Discover
    assert is_credit_card('6011 0009 9013 9424', 'DISCOVER')
    
    # Test with valid JCB
    assert not is_credit_card('3530 1113 3330 0000', 'JCB')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_invalid_inputs_error_handling.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_inputs_error_handling ______________________

    def test_invalid_inputs_error_handling():
        # Test with invalid card type
        with pytest.raises(KeyError):
            is_credit_card('4111 1111 1111 1111', 'INVALID_TYPE')
    
        # Test with empty string
        assert not is_credit_card('')
    
        # Test with non-numeric characters
        assert not is_credit_card('invalid input')
    
        # Test with valid VISA card
>       assert is_credit_card('4111 1111 1111 1111', 'VISA')
E       AssertionError: assert False
E        +  where False = is_credit_card('4111 1111 1111 1111', 'VISA')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_invalid_inputs_error_handling.py:28: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_invalid_inputs_error_handling.py::test_invalid_inputs_error_handling
============================== 1 failed in 0.03s ===============================
"""