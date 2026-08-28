
import pytest
from mimesis.providers.payment import Payment
from mimesis.enums import CardType
from mimesis.exceptions import NonEnumerableError


def test_credit_card_number_invalid_type():
    payment_instance = Payment()
    with pytest.raises(NonEnumerableError):
        payment_instance.credit_card_number("INVALID_TYPE")

def test_credit_card_number_visa():
    payment_instance = Payment()
    card_number = payment_instance.credit_card_number(CardType.VISA)
    assert isinstance(card_number, str), "Expected a string representation of the credit card number"
    assert len(card_number.replace(" ", "")) == 16, "Expected a 16-digit credit card number"
    assert card_number.startswith("4"), "Expected a Visa card number to start with '4'"


def test_credit_card_number_amex():
    payment_instance = Payment()
    card_number = payment_instance.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert isinstance(card_number, str), "Expected a string representation of the credit card number"
    assert len(card_number.replace(" ", "")) == 15, "Expected an American Express card number to be 15 digits long"
    assert card_number.startswith("34") or card_number.startswith("37"), "Expected an American Express card number to start with '34' or '37'"