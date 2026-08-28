
import pytest
from string_utils.validation import is_credit_card

def test_is_credit_card_basic():
    # Test a valid VISA card number without specifying card type
    assert is_credit_card('4111111111111111') == True

    # Test an invalid credit card number
    assert is_credit_card('1234567890123456') == False

    # Test a valid VISA card number specifying the card type
    assert is_credit_card('4111111111111111', 'VISA') == True

    # Test an invalid card number specifying the card type
    assert is_credit_card('1234567890123456', 'VISA') == False

    # Test a valid MasterCard number specifying the card type
    assert is_credit_card('5500000000000004', 'MASTERCARD') == True

    # Test an invalid card number specifying the card type
    assert is_credit_card('1234567890123456', 'MASTERCARD') == False

    # Test a valid American Express card number specifying the card type
    assert is_credit_card('378282246310005', 'AMERICAN_EXPRESS') == True

    # Test an invalid card number specifying the card type
    assert is_credit_card('123456789012345', 'AMERICAN_EXPRESS') == False

    # Test a valid Discover card number specifying the card type
    assert is_credit_card('6011111111111117', 'DISCOVER') == True

    # Test an invalid card number specifying the card type
    assert is_credit_card('1234567890123456', 'DISCOVER') == False

    # Test a valid JCB card number specifying the card type
    assert is_credit_card('3530111333300000', 'JCB') == True

    # Test an invalid card number specifying the card type
    assert is_credit_card('1234567890123456', 'JCB') == False

    # Test a valid Diners Club card number specifying the card type
    assert is_credit_card('30569309025904', 'DINERS_CLUB') == True

    # Test an invalid card number specifying the card type
    assert is_credit_card('12345678901234', 'DINERS_CLUB') == False

    # Test with an unsupported card type (should raise KeyError)
    with pytest.raises(KeyError):
        is_credit_card('4111111111111111', 'UNKNOWN_CARD_TYPE')
