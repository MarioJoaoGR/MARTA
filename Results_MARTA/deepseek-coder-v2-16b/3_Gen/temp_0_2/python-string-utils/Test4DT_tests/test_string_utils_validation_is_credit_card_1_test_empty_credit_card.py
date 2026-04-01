
import re
from unittest.mock import patch
from string_utils.validation import is_full_string

# Assuming CREDIT_CARDS is a dictionary mapping card types to regex patterns
CREDIT_CARDS = {
    'VISA': re.compile(r'^4[0-9]{12}(?:[0-9]{3})?$'),
    'MASTERCARD': re.compile(r'^5[1-5][0-9]{14}$'),
    'AMERICAN_EXPRESS': re.compile(r'^3[47][0-9]{13}$'),
    'DINERS_CLUB': re.compile(r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$'),
    'DISCOVER': re.compile(r'^6(?:011|5[0-9]{2})[0-9]{12}$'),
    'JCB': re.compile(r'^(?:2131|1800|35\d{3})\d{11}$')
}

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

def test_empty_credit_card():
    input_string = ''
    assert not is_credit_card(input_string), "Expected empty string to be invalid"
