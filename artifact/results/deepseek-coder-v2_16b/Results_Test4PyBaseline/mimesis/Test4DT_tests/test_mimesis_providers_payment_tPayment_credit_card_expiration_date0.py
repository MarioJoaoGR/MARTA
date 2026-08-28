
# Module: mimesis.providers.payment
import pytest
from mimesis.providers.payment import Payment
from mimesis import Person
from mimesis.enums import CardType, Gender

# Test initialization with default settings
def test_default_initialization():
    payment = Payment()
    assert isinstance(payment, Payment), "Initialization should create a Payment instance"