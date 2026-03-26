
import re
import pytest
from unittest.mock import patch

# Define regex patterns for different types of cards
VISA_PATTERN = r'^4[0-9]{12}(?:[0-9]{3})?$'
MASTERCARD_PATTERN = r'^(5[1-5][0-9]{14}|2(?:2[2-9]|[3-9][0-9])(?:[0-9]{12}))$'
AMEX_PATTERN = r'^3[47][0-9]{13}$'

# Function to check if a string is a valid credit card number
def is_credit_card(number):
    # Remove non-numeric characters for validation
    numeric_string = re.sub(r'[^0-9]', '', number)
    
    # Check length and pattern against known card types
    if len(numeric_string) == 16:
        if re.match(VISA_PATTERN, numeric_string):
            return True
        elif re.match(MASTERCARD_PATTERN, numeric_string):
            return True
        elif re.match(AMEX_PATTERN, numeric_string):
            return True
    return False

### Example Test Case for Updated Function
def test_valid_credit_card():
    assert is_credit_card('4111 1111 1111 1111') == True  # Valid Visa card
    assert is_credit_card('5555 5555 5555 4444') == True  # Valid MasterCard card
    assert is_credit_card('3782 822463 10005') == False   # Invalid American Express card (should be False)
