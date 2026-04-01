
import re

# Assuming CREDIT_CARDS is a dictionary mapping card types to their regex patterns
CREDIT_CARDS = {
    'VISA': re.compile(r'^4[0-9]{12}(?:[0-9]{3})?$'),
    'MASTERCARD': re.compile(r'^5[1-5][0-9]{14}$'),
    'AMERICAN_EXPRESS': re.compile(r'^3[47][0-9]{13}$'),
    'DINERS_CLUB': re.compile(r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$'),
    'DISCOVER': re.compile(r'^6(?:011|5[0-9]{2})[0-9]{12}$'),
    'JCB': re.compile(r'^35(?:28|29|30|31|32|33|34|35|36|37|38|39)[0-9]{12}$')
}

def is_full_string(input_string: str) -> bool:
    return input_string and not input_string.isspace()

def is_credit_card(input_string: str, card_type: str = None) -> bool:
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
            raise KeyError(
                'Invalid card type "{}". Valid types are: {}'.format(card_type, ', '.join(CREDIT_CARDS.keys()))
            )
        return CREDIT_CARDS[card_type].match(input_string) is not None

    for c in CREDIT_CARDS:
        if CREDIT_CARDS[c].match(input_string) is not None:
            return True

    return False

def test_valid_input_happy_path():
    # Test a valid VISA card
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

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        # Test a valid VISA card
>       assert is_credit_card('4111 1111 1111 1111', 'VISA') == True
E       AssertionError: assert False == True
E        +  where False = is_credit_card('4111 1111 1111 1111', 'VISA')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_happy_path.py:57: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.02s ===============================
"""