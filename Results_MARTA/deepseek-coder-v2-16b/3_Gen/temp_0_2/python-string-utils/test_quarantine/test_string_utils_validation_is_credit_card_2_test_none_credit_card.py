
from string_utils.validation import is_credit_card, CREDIT_CARDS
from unittest.mock import patch

def test_none_credit_card():
    with patch('string_utils.validation.is_full_string', return_value=True):
        assert not is_credit_card('4111 1111 1111 1111', 'VISA')
        assert not is_credit_card('5555 5555 5555 4444', 'MASTERCARD')
        assert not is_credit_card('3782 8224 6310 005', 'AMERICAN_EXPRESS')
        assert not is_credit_card('3056 9309 0259 04', 'DINERS_CLUB')
        assert not is_credit_card('6011 0009 9013 9424', 'DISCOVER')
        assert not is_credit_card('3530 1113 3330 0000', 'JCB')

        # Test with invalid card type
        try:
            is_credit_card('4111 1111 1111 1111', 'INVALID_TYPE')
        except KeyError as e:
            assert str(e) == 'Invalid card type "INVALID_TYPE". Valid types are: VISA, MASTERCARD, AMERICAN_EXPRESS, DINERS_CLUB, DISCOVER, JCB'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_none_credit_card.py F [100%]

=================================== FAILURES ===================================
____________________________ test_none_credit_card _____________________________

    def test_none_credit_card():
        with patch('string_utils.validation.is_full_string', return_value=True):
            assert not is_credit_card('4111 1111 1111 1111', 'VISA')
            assert not is_credit_card('5555 5555 5555 4444', 'MASTERCARD')
            assert not is_credit_card('3782 8224 6310 005', 'AMERICAN_EXPRESS')
            assert not is_credit_card('3056 9309 0259 04', 'DINERS_CLUB')
            assert not is_credit_card('6011 0009 9013 9424', 'DISCOVER')
            assert not is_credit_card('3530 1113 3330 0000', 'JCB')
    
            # Test with invalid card type
            try:
>               is_credit_card('4111 1111 1111 1111', 'INVALID_TYPE')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_none_credit_card.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_string = '4111 1111 1111 1111', card_type = 'INVALID_TYPE'

    def is_credit_card(input_string: Any, card_type: str = None) -> bool:
        """
        Checks if a string is a valid credit card number.
        If card type is provided then it checks against that specific type only,
        otherwise any known credit card number will be accepted.
    
        Supported card types are the following:
    
        - VISA
        - MASTERCARD
        - AMERICAN_EXPRESS
        - DINERS_CLUB
        - DISCOVER
        - JCB
    
        :param input_string: String to check.
        :type input_string: str
        :param card_type: Card type. Default to None (any card).
        :type card_type: str
    
        :return: True if credit card, false otherwise.
        """
        if not is_full_string(input_string):
            return False
    
        if card_type:
            if card_type not in CREDIT_CARDS:
>               raise KeyError(
                    'Invalid card type "{}". Valid types are: {}'.format(card_type, ', '.join(CREDIT_CARDS.keys()))
                )
E               KeyError: 'Invalid card type "INVALID_TYPE". Valid types are: VISA, MASTERCARD, AMERICAN_EXPRESS, DINERS_CLUB, DISCOVER, JCB'

python-string-utils/string_utils/validation.py:274: KeyError

During handling of the above exception, another exception occurred:

    def test_none_credit_card():
        with patch('string_utils.validation.is_full_string', return_value=True):
            assert not is_credit_card('4111 1111 1111 1111', 'VISA')
            assert not is_credit_card('5555 5555 5555 4444', 'MASTERCARD')
            assert not is_credit_card('3782 8224 6310 005', 'AMERICAN_EXPRESS')
            assert not is_credit_card('3056 9309 0259 04', 'DINERS_CLUB')
            assert not is_credit_card('6011 0009 9013 9424', 'DISCOVER')
            assert not is_credit_card('3530 1113 3330 0000', 'JCB')
    
            # Test with invalid card type
            try:
                is_credit_card('4111 1111 1111 1111', 'INVALID_TYPE')
            except KeyError as e:
>               assert str(e) == 'Invalid card type "INVALID_TYPE". Valid types are: VISA, MASTERCARD, AMERICAN_EXPRESS, DINERS_CLUB, DISCOVER, JCB'
E               assert "'Invalid car...ISCOVER, JCB'" == 'Invalid card...DISCOVER, JCB'
E                 
E                 - Invalid card type "INVALID_TYPE". Valid types are: VISA, MASTERCARD, AMERICAN_EXPRESS, DINERS_CLUB, DISCOVER, JCB
E                 + 'Invalid card type "INVALID_TYPE". Valid types are: VISA, MASTERCARD, AMERICAN_EXPRESS, DINERS_CLUB, DISCOVER, JCB'
E                 ? +                                                                                                                 +

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_none_credit_card.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_none_credit_card.py::test_none_credit_card
============================== 1 failed in 0.03s ===============================
"""