
import pytest
from mimesis.providers.payment import Payment
from mimesis import Person

# Test for generating a random PayPal email address
def test_paypal():
    payment = Payment()
    paypal_email = payment.paypal()
    assert isinstance(paypal_email, str), "Expected a string but got something else"
    assert '@' in paypal_email, "Expected an email address but it does not contain the '@' symbol"

# Test for invalid input to ensure TypeError is raised
def test_invalid_input_paypal():
    payment = Payment()
    with pytest.raises(TypeError):
        payment.paypal("invalid_input")
