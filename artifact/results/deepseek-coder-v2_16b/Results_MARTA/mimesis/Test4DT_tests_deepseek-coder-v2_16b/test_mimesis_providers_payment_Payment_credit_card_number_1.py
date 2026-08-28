
import pytest
from mimesis.providers.payment import Payment
from mimesis.enums import CardType
from mimesis.exceptions import NonEnumerableError

# Test default usage of credit_card_number method

# Test specific card type usage of credit_card_number method

# Test unsupported card type usage of credit_card_number method
def test_credit_card_number_unsupported_type():
    payment = Payment()
    with pytest.raises(NonEnumerableError):
        payment.credit_card_number('UnsupportedCardType')