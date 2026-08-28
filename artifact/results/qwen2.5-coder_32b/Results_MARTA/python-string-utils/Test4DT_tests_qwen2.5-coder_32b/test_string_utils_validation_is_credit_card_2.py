
import pytest
from string_utils.validation import is_credit_card

def test_is_credit_card_basic():
    # Test a valid VISA card number without specifying card type
    assert is_credit_card('4111111111111111') == True
    
    # Test an invalid credit card number
    assert is_credit_card('1234567890123456') == False

    # Test a valid VISA card number specifying the card type
    assert is_credit_card('4111111111111111', 'VISA') == True
    
    # Test an invalid card type
    with pytest.raises(KeyError):
        is_credit_card('4111111111111111', 'UNKNOWN_CARD_TYPE')
