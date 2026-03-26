
import re
import pytest

# Updated regex patterns for different card types
VISA_REGEX = r'^4[0-9]{12}(?:[0-9]{3})?$'
MASTERCARD_REGEX = r'^(5[1-5][0-9]{14}|2[2-7][0-9]{14})$'
AMERICAN_EXPRESS_REGEX = r'^3[47][0-9]{13}$'
DINERS_CLUB_REGEX = r'^(30[0-5]|36[0-9])[0-9]{12}$'
DISCOVER_REGEX = r'^6(?:011|5[0-9]{2})[0-9]{12}$'
JCB_REGEX = r'^(?:(?:2131|1800)[0-9]{11}|35\d{14})$'

# Function to validate credit card numbers using regex patterns
def is_credit_card(number):
    number = re.sub(r'\D', '', number)  # Remove non-digit characters
    if not (len(number) >= 13 and len(number) <= 19):
        return False
    return bool(re.match(VISA_REGEX, number)) or \
           bool(re.match(MASTERCARD_REGEX, number)) or \
           bool(re.match(AMERICAN_EXPRESS_REGEX, number)) or \
           bool(re.match(DINERS_CLUB_REGEX, number)) or \
           bool(re.match(DISCOVER_REGEX, number)) or \
           bool(re.match(JCB_REGEX, number))

# Example Test Case with Correct Data
@pytest.mark.parametrize("number, expected", [
    ('4111 1111 1111 1111', True),  # Valid Visa
    ('5555 5555 5555 4444', True),  # Valid MasterCard
    ('3782 822463 10005', True),   # Valid American Express
    ('3056 930902 5904', True),   # Valid Diners Club
    ('6011 0009 9013 9424', True), # Valid Discover
    ('3530 1113 3330 0000', True), # Valid JCB
    ('1234 5678 9012 3456', False), # Invalid number, length too short
    ('1234 5678 9012 34567890', False) # Invalid number, length too long
])
def test_is_credit_card(number, expected):
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_credit_card_0
python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0.py:36:43: E0001: Parsing failed: 'expected an indented block after function definition on line 36 (Test4DT_tests.test_string_utils_validation_is_credit_card_0, line 36)' (syntax-error)

"""