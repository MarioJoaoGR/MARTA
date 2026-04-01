
import re
from string_utils.validation import is_full_string, CREDIT_CARDS

def is_credit_card(input_string: str, card_type: str = None) -> bool:
    """
    Checks if a string is a valid credit card number. If a specific card type is provided, it checks against that type only; otherwise, it accepts any known credit card number.

    Supported card types are VISA, MASTERCARD, AMERICAN_EXPRESS, DINERS_CLUB, DISCOVER, and JCB.

    :param input_string: The string to check, which should represent a credit card number.
    :type input_string: str
    :param card_type: Optional parameter specifying the type of credit card to validate against. Default is None, allowing any valid credit card.
    :type card_type: str

    :return: True if the string is a valid credit card number for the specified type or if no specific type is provided and it matches any known card type; False otherwise.
    """
    if not is_full_string(input_string):
        return False

    if card_type:
        if card_type not in CREDIT_CARDS:
            raise KeyError(f'Invalid card type "{card_type}". Valid types are: {", ".join(CREDIT_CARDS.keys())}')
        return bool(CREDIT_CARDS[card_type].match(input_string))

    for c in CREDIT_CARDS:
        if bool(CREDIT_CARDS[c].match(input_string)):
            return True

    return False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.02s =============================
"""